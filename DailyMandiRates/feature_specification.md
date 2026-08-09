# MandiCheck (منڈی چیک) — Daily DC & Mandi Rates Spec

## Executive Overview & Vision
**MandiCheck (منڈی چیک)** is an automated, AI-powered daily commodity price extraction pipeline, administrative validation dashboard, and consumer transparency mobile application designed specifically for the Pakistani agricultural market.

District Commissioner (DC) offices across Pakistan issue official retail ceiling price lists daily for essential fresh commodities (vegetables, fruits, poultry, grains). However, these lists are published as low-quality scanned PDFs or mobile camera shots of printed sheets, often containing stamp overlays, handwritten corrections, and mixed Urdu/English layouts. Manual data entry is slow, causing delays that enable retail price gouging. Furthermore, wholesale prices fluctuate hourly in local markets (*Sabzi Mandis*) based on morning auctions, creating a massive disparity between official retail ceilings and actual wholesale costs.

MandiCheck solves these pain points by building an automated multimodal Vision AI extraction pipeline that ingests daily scanned rate lists, parses commodity prices, stores them in a normalized database, and exposes them via a consumer mobile app and administrative dashboard.

---

## 1. Targeted Local Context & Critical Metrics
The app is tailored to the specific characteristics of the Pakistani agricultural trading system:
*   **Wholesale vs. DC Retail Variance**: Computes the difference between wholesale Mandi auction rates and the official DC retail price ceiling. This warns consumers when retailers are overcharging, and alerts magistrates when wholesale costs exceed the retail ceiling (which causes artificial supply shortages).
*   **Bilingual Extraction & Standardized Units**: Normalizes varying local trade units: Kilogram (کلو), Dozen (درجن), Mann/40kg (من), Crate/Box (پیٹی), and Dhari/5kg (دھڑی).
*   **Urdu Nastaliq RTL Rendering**: Custom mobile UI utilizing native Nastaliq font styles, ensuring clean, legible Urdu reading for shopkeepers and consumers.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on establishing the automated Vision AI parser, the human-in-the-loop operator validation dashboard, and a bilingual mobile directory with offline caching.

### A. Automated AI Vision Extraction Pipeline
*   **Multi-Source Document Ingestion**: Ingests daily price list scans via DC website scrapers, district WhatsApp groups, or manual admin uploads.
*   **Bilingual Multimodal OCR**: Employs advanced Vision LLMs (e.g., Claude 3.5 Sonnet / GPT-4o Vision API) to convert low-quality scans into structured JSON, mapping varying columns (Item Name, Grade, Wholesale Min/Max, DC Retail Price, Unit).
*   **Unit & District Normalization**: Normalizes Urdu titles (e.g., ٹماٹر / Tomato) and maps local units to a standardized dictionary.

### B. Human-in-the-Loop (HITL) Admin Dashboard
*   **Split-Screen Validator**: Display a side-by-side comparison of the raw scanned image against the extracted table rows.
*   **Confidence Score Flagging**: Automatically highlights rows where Vision AI confidence falls below 85% due to overwritten stamps or blurry handwriting.
*   **One-Click Publishing**: Allows operator review, correction, and publishing to the live mobile app within 60 seconds.

### C. Core Mobile UX & Features
*   **District & Category Filters**: Search commodity rates by District (Lahore, Karachi, Rawalpindi, Peshawar, etc.) and category (Vegetables, Fruits, Grains, Poultry).
*   **Price Variance Indicators**: Displays active warnings when the variance between wholesale mandi rates and retail ceilings is unusually high.
*   **Bilingual Nastaliq UI**: Complete Urdu and English interface toggle.
*   **Room DB Caching**: Caches daily lists locally, allowing users to check official rates in rural markets with poor internet connectivity.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app integrates public violation reporting, middleman margin maps, automated WhatsApp rate lookup bots, and AI price forecasting.

### A. Price Gouging Violation Reporting
*   **Magistrate Reporting Channel**: Allows consumers to take photos of retail shop price boards and upload their purchase bills. The app pre-fills a complaint form detailing the overcharge amount and submits it directly to local Price Control Magistrates.

### B. Middleman Profit Spread Maps
*   **Price Spread Analytics**: Displays interactive heatmaps illustrating the profit margin spread pocketed by middlemen and retail merchants across different cities.

### C. Automated WhatsApp Rate Bot
*   **WhatsApp Webhook lookup**: Diners and vendors text a commodity and city name (e.g., *"Rawalpindi Onion rate"* or *"راولپنڈی پیاز کا ریٹ"*) to a verified WhatsApp business number, receiving the official DC retail price and morning Mandi average rate instantly.

### D. Seasonal Price Trend Predictor
*   **AI Price Forecaster**: Analyzes historical market logs to predict upcoming price hikes based on weather forecasts (e.g., monsoon rains flooding crop fields in Sindh) or cultural demand shifts (e.g., lemon/onion spikes during Ramadan and Eid).

---

## 4. Proposed Database Schema Design

### districts
| Field Name | Type | Description |
|---|---|---|
| id | UUID (PK) | Unique ID |
| name_en | VARCHAR(100) | English Name (e.g., Rawalpindi) |
| name_ur | VARCHAR(100) | Urdu Name (e.g., راولپنڈی) |
| province | VARCHAR(50) | Punjab, Sindh, KPK, Balochistan, ICT |

### commodities
| Field Name | Type | Description |
|---|---|---|
| id | UUID (PK) | Unique ID |
| category | ENUM | vegetable, fruit, grain, poultry |
| name_en | VARCHAR(100) | English Name (e.g., Tomato) |
| name_ur | VARCHAR(100) | Urdu Name (e.g., ٹماٹر) |
| standard_unit | VARCHAR(20) | Default base unit (kg, dozen, 40kg) |

### daily_rate_lists
| Field Name | Type | Description |
|---|---|---|
| id | UUID (PK) | Unique ID |
| district_id | FK (districts) | Reference to District |
| issuance_date | DATE | Date of list issue |
| source_image_url | TEXT | Storage link to raw scan |
| status | ENUM | pending_review, published, rejected |
| uploaded_at | TIMESTAMP | System timestamp |

### commodity_rates
| Field Name | Type | Description |
|---|---|---|
| id | UUID (PK) | Unique ID |
| rate_list_id | FK (daily_rate_lists) | Parent Rate List |
| commodity_id | FK (commodities) | Master Commodity Reference |
| grade | VARCHAR(20) | Grade A / Special / FAQ |
| unit | VARCHAR(20) | Unit specified in scan (kg, mann, crate) |
| wholesale_min | DECIMAL(10,2) | Minimum Mandi Rate |
| wholesale_max | DECIMAL(10,2) | Maximum Mandi Rate |
| dc_retail_price | DECIMAL(10,2) | Fixed DC Retail Rate |
| ocr_confidence | DECIMAL(5,2) | Extraction accuracy score (0 - 100%) |

---

## 5. Recommended Tech Stack
*   **Mobile App**: Flutter (supporting Nastaliq font styles and Room DB cache equivalent).
*   **Backend API**: Python (FastAPI) or Node.js (TypeScript).
*   **Database**: PostgreSQL (with PostGIS for location-aware district lookup) + Redis (caching daily rates).
*   **AI Vision Pipeline**: Claude 3.5 Sonnet Vision API / GPT-4o Vision API for zero-shot structured JSON parsing.