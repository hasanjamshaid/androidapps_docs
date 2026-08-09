# Technical Details Document: TenderCheck (ٹینڈر چیک)

This document provides the technical specifications, database models, scraping architectures, AI bidding document parsers, and client-server integration protocols for **TenderCheck (ٹینڈر چیک)**. The system is built using a **Next.js Web UI** inside an **Android WebView Wrapper** shell, backed by serverless **AWS Lambda** microservices, **PostgreSQL** (with **PostGIS**), **Elasticsearch**, and **Meta's WhatsApp Cloud API**.

---

## 1. System Architecture & Crawling Pipeline

TenderCheck consolidates procurement advertisements from Federal and Provincial PPRA portals, standardizing various HTML tables and document types into a single indexed database.

```mermaid
graph TD
    %% Scraping Tier
    subgraph Scheduled Scraping Suite (AWS EventBridge / Lambda)
        FedScraper[Federal PPRA Crawler] -->|Crawl ppra.gov.pk| RawTenders[Raw Scraped HTML]
        PbScraper[Punjab PPRA Crawler] -->|Crawl ppra.punjab.gov.pk| RawTenders
        SindhScraper[Sindh SPPRA Crawler] -->|Crawl sppra.org.pk| RawTenders
        KPKScraper[KP KPPRA Crawler] -->|Crawl kppra.gov.pk| RawTenders
        BalScraper[Balochistan BPPRA Crawler] -->|Crawl bppra.gob.pk| RawTenders
    end

    %% Ingestion Tier
    RawTenders --> PDFDownloader[PDF Downloader Lambda]
    PDFDownloader -->|Fetch Tender Notices & RFPs| S3Bucket[Secure S3 Storage]
    S3Bucket --> DocumentParser[AI PDF BOQ/RFP Parser Lambda]
    DocumentParser -->|Gemini API Integration| StructuredTender[Normalized JSON Tenders]

    %% Storage Tier
    StructuredTender --> Postgres[(PostgreSQL DB<br/>PostGIS Spatial)]
    StructuredTender --> IndexES[(Elasticsearch Cluster)]

    %% Alerting Tier
    Postgres --> AlertWorker[WhatsApp Alert Worker Lambda]
    AlertWorker -->|Match Keywords & PEC Ranks| WAAPI[WhatsApp Cloud API]
    WAAPI --> ContractorWA[Contractor WhatsApp Notifications]

    %% Client Tier
    Client[Next.js WebView Client] <-->|Search & Filter Tenders| APIGateway[AWS API Gateway]
    APIGateway <--> DiscoveryAPI[Tender Discovery Lambda]
    DiscoveryAPI --> Postgres
    DiscoveryAPI --> IndexES

    style DocumentParser fill:#ffe0b2,stroke:#fb8c00,stroke-width:2px
    style S3Bucket fill:#ffccbc,stroke:#e64a19,stroke-width:1px
    style AlertWorker fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    style Postgres fill:#ede7f6,stroke:#5e35b1,stroke-width:2px
```

---

## 2. Database Schema & Data Models

### A. PostgreSQL Schema (Relational Store)
Tracks tender details, PEC requirements, bidding criteria, contractor registration details, and WhatsApp keywords subscriptions.

```sql
-- Private/Public Procurement Portals
CREATE TABLE procurement_portals (
    portal_id VARCHAR(50) PRIMARY KEY, -- e.g., 'fed_ppra', 'punjab_ppra', 'sindh_sppra', 'kppra', 'bppra'
    portal_name VARCHAR(150) NOT NULL,
    base_url VARCHAR(255) NOT NULL
);

-- Normalized Government Departments
CREATE TABLE government_departments (
    dept_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    dept_name VARCHAR(255) UNIQUE NOT NULL, -- e.g., 'Communication & Works (C&W) Department', 'WAPDA'
    city VARCHAR(100) NOT NULL
);

-- Consolidated Tenders Table
CREATE TABLE tenders (
    tender_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    portal_id VARCHAR(50) REFERENCES procurement_portals(portal_id) ON DELETE RESTRICT,
    dept_id UUID REFERENCES government_departments(dept_id) ON DELETE CASCADE,
    tender_ref_number VARCHAR(100) NOT NULL, -- Unique registration code from PPRA
    title TEXT NOT NULL,
    description_raw TEXT,
    estimated_cost_pkr NUMERIC(15, 2), -- NULL if cost is not disclosed
    earnest_money_pkr NUMERIC(12, 2), -- Bid Security deposit (CDR)
    pec_category_required VARCHAR(10), -- e.g., 'C6', 'C5', 'C3', 'CA'
    pec_codes_required VARCHAR(50)[], -- Array of codes (e.g. ['CE01', 'EE01'])
    publish_date DATE NOT NULL,
    submission_deadline TIMESTAMP WITH TIME ZONE NOT NULL,
    bidding_document_url VARCHAR(512), -- Link to download PDF
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Contractor Eligibility Profiles
CREATE TABLE contractor_profiles (
    profile_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID UNIQUE NOT NULL,
    pec_category VARCHAR(10) NOT NULL, -- e.g. 'C5'
    pec_specialized_codes VARCHAR(50)[], -- e.g. ['CE01', 'CE02', 'EE11']
    is_active_taxpayer BOOLEAN DEFAULT FALSE, -- FBR active filer
    pra_registered BOOLEAN DEFAULT FALSE, -- Punjab Revenue Authority
    srb_registered BOOLEAN DEFAULT FALSE, -- Sindh Revenue Board
    kpra_registered BOOLEAN DEFAULT FALSE, -- KP Revenue Authority
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- WhatsApp Keywords Alert Subscriptions
CREATE TABLE alert_subscriptions (
    subscription_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES contractor_profiles(user_id) ON DELETE CASCADE,
    phone_number VARCHAR(50) NOT NULL,
    keywords VARCHAR[] NOT NULL, -- e.g., ['road', 'bridge', 'transformer', 'solar']
    is_enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. Web Scraping & Normalization Engine

Government PPRA websites often use legacy structures, CAPTCHAs, or ASP.NET postback pagination controls. 

### A. Python PPRA Crawler (Handling Postback ViewStates)
The crawler simulates session state postbacks using Python's `requests` library to navigate the tables.

```python
import requests
from bs4 import BeautifulSoup

def scrape_punjab_ppra_tenders():
    url = "https://ppra.punjab.gov.pk/active_tenders"
    session = requests.Session()
    
    # 1. Establish session and extract ASP.NET viewstates
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    viewstate = soup.find('input', id='__VIEWSTATE')['value']
    viewstategenerator = soup.find('input', id='__VIEWSTATEGENERATOR')['value']
    eventvalidation = soup.find('input', id='__EVENTVALIDATION')['value']
    
    # 2. Post payload requesting next page of tables
    payload = {
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': viewstategenerator,
        '__EVENTVALIDATION': eventvalidation,
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$GridView1',
        '__EVENTARGUMENT': 'Page$2' # Request page 2
    }
    
    post_response = session.post(url, data=payload)
    parsed_page = BeautifulSoup(post_response.content, 'html.parser')
    
    scraped_tenders = []
    # Parse rows in GridView table
    for row in parsed_page.find_all('tr', class_='grid-row-style'):
        cols = row.find_all('td')
        if len(cols) >= 5:
            ref_num = cols[0].text.strip()
            org_name = cols[1].text.strip()
            tender_title = cols[2].text.strip()
            deadline = cols[3].text.strip()
            doc_link = cols[4].find('a')['href'] if cols[4].find('a') else None
            
            scraped_tenders.append({
                "ref_num": ref_num,
                "org": org_name,
                "title": tender_title,
                "deadline": deadline,
                "document_url": doc_link
            })
            
    return scraped_tenders
```

---

## 4. AI RFP & BOQ PDF Document Parser (Gemini Integration)

Once a tender is discovered, the **PDF Downloader Lambda** fetches the RFP/BOQ document. The **AI Parser Lambda** extracts required qualifications using Gemini.

### Gemini RFP Parser System Prompt Template
```text
You are an expert procurement auditor. Analyze this government RFP/BOQ document snippet and extract the contractor requirements.

RULES:
1. Identify the minimum PEC (Pakistan Engineering Council) category required (C6 to CA).
2. Locate the specific PEC specialized codes (e.g. CE01 for Road construction, EE11 for Solar power).
3. Find the Earnest Money (Bid Security) required (percentage of estimate or absolute PKR value).
4. Extract the minimum required years of relevant experience.
5. Output MUST conform strictly to the JSON schema.

JSON Output Schema:
{
  "pec_category_required": "C6 | C5 | C4 | C3 | C2 | C1 | CO | CA",
  "pec_specialized_codes": ["String"],
  "earnest_money_pkr": 0.00,
  "experience_years_required": 0,
  "required_documents": ["String"],
  "confidence_score": 0.0 to 1.0
}
```

---

## 5. PEC Category Eligibility Matching Algorithm

The eligibility engine compares a contractor's category limits and code specifications against target tenders.

### PEC Category Limits & Code Matching Matrix
*   **CA**: Unlimited
*   **CB**: Up to Rs. 4,000 Million
*   **C1**: Up to Rs. 2,500 Million
*   **C2**: Up to Rs. 1,000 Million
*   **C3**: Up to Rs. 500 Million
*   **C4**: Up to Rs. 200 Million
*   **C5**: Up to Rs. 65 Million
*   **C6**: Up to Rs. 25 Million

### TypeScript Eligibility Evaluator (`lib/eligibility-matcher.ts`)
```typescript
type PECCategory = 'C6' | 'C5' | 'C4' | 'C3' | 'C2' | 'C1' | 'CB' | 'CA';

const categoryHierarchy: Record<PECCategory, number> = {
  'C6': 1,
  'C5': 2,
  'C4': 3,
  'C3': 4,
  'C2': 5,
  'C1': 6,
  'CB': 7,
  'CA': 8
};

export class PECEligibilityMatcher {
  
  public static isEligible(
    contractorCategory: PECCategory,
    contractorCodes: string[],
    tenderCategoryRequired: PECCategory,
    tenderCodesRequired: string[],
    tenderCostPKR: number
  ): { eligible: boolean; reason: string } {
    
    // 1. Check Category Rank Hierarchy (Contractor rank must be >= Tender requirement rank)
    const contractorRank = categoryHierarchy[contractorCategory];
    const tenderRank = categoryHierarchy[tenderCategoryRequired];
    
    if (contractorRank < tenderRank) {
      return { 
        eligible: false, 
        reason: `Required PEC category is ${tenderCategoryRequired}, but company is registered as ${contractorCategory}.` 
      };
    }

    // 2. Check specialized work code compliance
    const hasAllCodes = tenderCodesRequired.every(code => contractorCodes.includes(code));
    if (!hasAllCodes) {
      const missingCodes = tenderCodesRequired.filter(code => !contractorCodes.includes(code));
      return {
        eligible: false,
        reason: `Company lacks required specialized PEC codes: ${missingCodes.join(', ')}.`
      };
    }

    return { eligible: true, reason: "Eligible to bid." };
  }
}
```

---

## 6. WhatsApp Alerts & Push Notifications

When a new tender is indexed, the **Alert Worker Lambda** queries active user keyword subscriptions. If a match is found, it sends an alert via Meta's WhatsApp Cloud API.

### Meta WhatsApp Request Payload
```json
{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "+923001234567",
  "type": "template",
  "template": {
    "name": "tendercheck_new_alert",
    "language": { "code": "ur_PK" }, -- Urdu localized notification template
    "components": [
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "Communication & Works (C&W)" },
          { "type": "text", "text": "Road construction from Lahore to Multan" },
          { "type": "text", "text": "C5" },
          { "type": "text", "text": "25th Aug, 2026" }
        ]
      }
    ]
  }
}
```

---

## 7. API Reference Specification

### A. Search Tenders Index
`GET /api/tenders/search`

#### Query Parameters:
*   `user_id`: Unique identifier (for auto-eligibility mapping)
*   `query`: Keyword string (e.g. `bridge`)
*   `portal_id`: Optional portal constraint (e.g. `sindh_sppra`)
*   `max_cost`: Cost ceiling limit (e.g. `50000000` PKR)

#### Response Payload (200 OK):
```json
{
  "tenders_matched": 1,
  "contractor_eligibility_override": "ELIGIBLE",
  "results": [
    {
      "tender_id": "4d112-4462-8b22-83b3b27bcfb9",
      "tender_ref_number": "PPRA-WAPDA-2026-92",
      "title": "Installation of 100kW Grid-Connected Solar System",
      "department": "Water & Power Development Authority (WAPDA)",
      "estimated_cost_pkr": 18000000.00,
      "earnest_money_pkr": 360000.00, -- 2% CDR requirement calculated
      "pec_category_required": "C6",
      "pec_codes_required": ["EE11"],
      "submission_deadline": "2026-08-25T11:00:00Z",
      "bidding_document_url": "https://ppra.gov.pk/documents/wapda_solar_spec.pdf",
      "eligibility_check": {
        "is_eligible": true,
        "reason": "Contractor holds C5 rank (which qualifies for C6 limit of 25M) and includes the EE11 specialized code."
      }
    }
  ]
}
```

### B. Fetch Bidding Document Summary
`GET /api/tenders/document-summary`

#### Query Parameters:
*   `tender_id`: Target ID

#### Response Payload (200 OK):
```json
{
  "tender_id": "4d112-4462-8b22-83b3b27bcfb9",
  "document_summary": {
    "extracted_experience_required": "Minimum 3 years in solar grid-tie works.",
    "pec_category_required": "C6",
    "pec_codes_required": ["EE11"],
    "required_checklist": [
      "Original CDR (Call Deposit Receipt) of 360,000 PKR",
      "Active FBR Filer Certificate",
      "Active PRA (Punjab Revenue Authority) registration certificate",
      "Affidavit of Non-Blacklisting"
    ]
  }
}
```
