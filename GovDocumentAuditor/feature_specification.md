# AsaanSarkari (آسان سرکاری) — Pakistan Government Document Auditor Spec

## Executive Overview & Vision
**AsaanSarkari (آسان سرکاری)** is an independent, crowdsourced government document fee index, step-by-step procedural roadmap, public office queue tracker, and anti-corruption audit mobile application designed specifically for Pakistani citizens.

Applying for basic legal and administrative documents in Pakistan (e.g., driving licenses, gun licenses, domicile certificates, birth/marriage certificates, land registration copies/Fard, vehicle registration, and international passport renewals) is a confusing and opaque process. This lack of transparency has enabled a thriving, exploitative ecosystem:
*   **The Tout & Agent Mafia**: Outside government offices (Excise & Taxation, Passport Offices, NADRA centers, Patwarkhanas), unauthorized local agents set up desks and charge massive markups (often 300% to 500% of official fees) to "facilitate" files, claiming the process is impossible without bribes.
*   **Opaque Fee Schedules**: Official fee structures are scattered across outdated government portals or hidden within complex bank challan codes (NBP/SBP challans, PSID codes). Citizens routinely pay double or triple the actual legal fee without knowing it.
*   **Digital Payment Barriers**: Homeowners and drivers struggle to navigate new online payment portals like e-Pay Punjab, e-Pay Sindh, and federal FBR portals.

AsaanSarkari solves these challenges by providing a unified fee directory, bilingual step-by-step procedure checklists, crowdsourced queue wait trackers, and anonymous bribe/extortion mapping.

---

## 1. Targeted Local Context & Critical Metrics
The app is tailored to the specific administrative and provincial regulations of the Pakistani public sector:
*   **Province-Filtered Fee Directory**: Lists exact fees, stamp duties, and mandatory government challans by province (Punjab, Sindh, KPK, Balochistan, and Islamabad Capital Territory - ICT).
*   **Filer vs. Non-Filer Tax Calculator**: Computes stamp duties and registration taxes for vehicles and properties, dynamically adjusting based on the user's active FBR Filer status.
*   **Digital Payment Challan Guides**: Step-by-step walkthroughs explaining how to generate PSID codes on e-Pay portals, make payments via mobile banking, or fill out paper National Bank of Pakistan (NBP) challan forms.
*   **Agent & Extortion Reporting Map**: Maps reported locations where touts operate or where public officials demand bribes to process documents.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a province-filtered fee directory, bilingual step-by-step procedure guides, a local office directory, and offline caching.

### A. Core Directories & Checklists
*   **Unified Fee Index**: A searchable directory of exact official rates for 50+ basic documents, licenses, and certificates. Includes tax calculations based on active Filer status.
*   **Bilingual Procedure Roadmaps**: Step-by-step procedural guides (Urdu Nastaliq and English) showing exactly what forms to print, how to pay (PSID, e-Pay, bank counters), which counters to visit in order, biometric queues, and official approval times.
*   **Office Locator & Hours**: Directories of local NADRA mega centers, Passport Offices, Excise Offices, and DLIMS driving license centers.

### B. Mobile UI & Bilingual Support
*   **Nastaliq Urdu UI**: High-legibility Urdu interface toggle utilizing native Nastaliq font styles.
*   **Offline Room DB Cache**: Stores fee tables, challan codes, and counter guides locally, ensuring citizens can check document guidelines inside thick-walled government buildings with no internet signal.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces crowdsourced office wait trackers, anonymous bribe mapping, and interactive required document checkers.

### A. Crowdsourced Office Wait Time & Token Tracker
*   **Real-Time Queue Tracker**: Allows users to log their arrival times, current token numbers, and final exit times at specific centers. Displays live wait estimates (e.g., *"NADRA Mega Center Blue Area Islamabad: Average token queue wait is 1.5 hours, card printing backlog is 12 days"*).

### B. Extortion & Agent Bribe Reporting Map
*   **Corruption Heatmaps**: An anonymous reporting submission feed where citizens can log instances of touts demanding money, public officials asking for bribes, or illegal extra charges. The data generates a geographic heatmap highlighting high-risk government branches to help citizens avoid them.

### C. Interactive Required Document Checklist
*   **Smart Document Checker**: Users input their specific task (e.g., *"Renewing a minor passport with a single parent present"* or *"Registering an imported vehicle in Sindh"*). The app generates a customized, mandatory checklist of required documents (CNIC copies, B-Forms, parent presence rules, NOC letters) to prevent counter rejections.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing province-specific fee schemas and coordinates of government offices, synced to the client Room DB SQLite cache.
*   **Scraper Worker**: Python-based scraper that crawls official government gazettes, DLIMS, NADRA, and provincial excise web pages weekly to update fee charts.
*   **Anonymity Engine**: Bribe reports strip all user metadata (IP address, user ID, device ID) before storing them in the database to guarantee reporter safety.