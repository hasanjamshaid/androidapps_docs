# TenderCheck (ٹینڈر چیک) — Pakistan PPRA Tender Scraper & Alerts Spec

## Executive Overview & Vision
**TenderCheck (ٹینڈر چیک)** is an automated daily public procurement scraper, contractor eligibility matcher, AI-powered bidding document parser, and real-time WhatsApp alert mobile application designed specifically for contractors and suppliers in Pakistan.

Navigating public sector contracting in Pakistan is a complex and highly fragmented process:
*   **Decentralized PPRA Portals**: Government tenders are published across multiple, disconnected portals: Federal PPRA (*ppra.gov.pk*), Punjab PPRA (*ppra.punjab.gov.pk*), Sindh SPPRA (*sppra.org.pk*), Khyber Pakhtunkhwa KPPRA (*kppra.gov.pk*), and Balochistan BPPRA (*bppra.gob.pk*).
*   **Outdated Search Systems**: Existing PPRA sites are extremely slow, have search engines that regularly fail, and require contractors to manually download and scan dozens of PDF notices daily.
*   **Confusing Eligibility Criteria**: Tenders demand specific compliance: Pakistan Engineering Council (PEC) builder category ranks (from C6 up to CA), FBR active taxpayer status, provincial sales tax registration (PRA/SRB/KPRA), and earnest money (bid security) bank deposits (CDRs).
*   **Missed Deadlines**: Contractors frequently miss lucrative government contracts simply because they didn't check the specific department sub-pages before the submission deadline.

TenderCheck solves these challenges by compiling all federal and provincial tenders into a single searchable directory, matching tenders to the contractor's specific PEC/FBR profile, and sending real-time keyword alerts.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the regulatory and administrative parameters of the Pakistani public procurement system:
*   **Centralized PPRA Scraper Directory**: Automatically crawls and normalizes daily tender ads from Federal PPRA, Punjab PPRA, Sindh SPPRA, KPK KPPRA, and Balochistan BPPRA.
*   **PEC Category Mapping**: Filters tenders based on Pakistan Engineering Council (PEC) ranks (C6, C5, C4, C3, C2, C1, CO, CA) and specialized codes (e.g., CE01 Road construction, EE01 Electrical works).
*   **Bid Security (CDR) Tracker**: Logs estimated project costs and calculates the required Call Deposit Receipt (CDR) earnest money (typically 2% to 5% of the total estimate).
*   **Bilingual Interface**: Native Urdu and English toggle using Nastaliq font styles.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a centralized PPRA tender directory, dynamic eligibility filters, a bilingual interface, and offline caching.

### A. Core Scraper & Search Directory
*   **Centralized Tender Directory**: A searchable index aggregating daily tenders from Federal and Provincial PPRA portals.
*   **Dynamic Search Filters**: Filter tenders by City, Government Department (e.g., Communications & Works (C&W), WAPDA, Health Department, Irrigation), Estimated Cost, Bid Security, PEC Category, and Submission Deadline.
*   **Offline Cache (Room DB)**: Caches bookmarked tenders, department contacts, and recent search profiles locally for offline contractor access.

### B. Mobile UI & Bilingual Support
*   **Nastaliq Urdu UI**: High-legibility Urdu interface toggle utilizing native Nastaliq font styles.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces AI bid document parsers, contractor eligibility profile matchers, instant WhatsApp alerts, and bid countdown planners.

### A. AI Bid Document Parser (OCR & Summarizer)
*   **RFP & BOQ Summary Extractor**: In-app PDF parser (Gemini) that reads downloaded bidding documents (RFPs/BOQs), extracts critical criteria (e.g. required experience, PEC category, bid security) and presents them as simple, clean bullet points.

### B. Contractor Eligibility Profile (FBR & PEC Matcher)
*   **Eligibility Matcher**: Contractor inputs their company profile (PEC category, FBR Filer status, provincial active tax registrations). The app automatically flags active tenders they are eligible to bid for, hiding irrelevant listings.

### C. Instant WhatsApp & Email Alerts
*   **Keyword Alert Bot**: Sends push notifications or WhatsApp messages to contractors the instant a new tender matching their selected keywords (e.g., "road construction", "IT equipment supply", "software development") is published.

### D. Bid Submission Countdown & Checklist Planner
*   **Bid Prep Checklist**: Active countdown trackers for bid submission times, with interactive checklists for preparing bid packages (CDR draft, PEC certificate, FBR filer certificates, affidavit).

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing processed de-biased news records, daily exchange rates, and historical logs, synced to the client Room DB SQLite cache.
*   **NLP Pipeline**: Python-based scraper running hourly, parsing HTML/RSS feeds, checking duplicate articles via semantic embedding matching, and summarizing via Gemini API before admin validation.
*   **On-Device Privacy**: No tracking of user political preferences. Search history and read bookmarks are stored strictly on the client Room DB SQLite database.
