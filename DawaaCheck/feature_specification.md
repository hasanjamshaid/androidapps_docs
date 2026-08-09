# DawaaCheck (دوا چیک) — Pakistan Medicine & Price Verifier Spec

## Executive Overview & Vision
**DawaaCheck (دوا چیک)** is a healthcare utility and price intelligence mobile application designed specifically for Pakistani patients and consumers.

The pharmaceutical retail sector in Pakistan suffers from major systemic issues that directly impact public health and consumer finances:
*   **Counterfeit & Unregistered Medicines**: Weak supply chains lead to fake or substandard medicines flooding local markets.
*   **Arbitrary Price Gouging**: Retail pharmacies frequently sell medicines above the Maximum Retail Price (MRP) regulated by the Drug Regulatory Authority of Pakistan (DRAP), especially during supply chain bottlenecks.
*   **Frequent Shortages**: Crucial medicines (e.g., Panadol, insulin, inhalers) frequently go out of stock due to price disputes or raw material import issues. Patients are often left stranded, unaware of identical substitutes.

DawaaCheck protects consumers by offering instant verification of DRAP registration, official price check limits, and chemical generic brand matches to counter local shortages.

---

## 1. Targeted Local Context & Critical Metrics
The app evaluates and verifies Pakistani medicines based on official regulations:
*   **DRAP Registration Status**: Verifies if the product has a valid, active Drug Regulatory Authority of Pakistan (DRAP) Registration Number (D.R. No.).
*   **Official MRP Price Limit**: Displays the government-controlled price per individual tablet/capsule/bottle and per total pack to prevent retail overcharging.
*   **Identical Generic Substitutes**: Maps brand names to their active chemical formulas, displaying matching alternative brands with identical strengths (e.g., 500mg) and dosage forms (e.g., tablet, syrup, suspension).
*   **Urdu & English Patient Safety Guides**: Simple translation of dosing instructions, precautions, and contraindications (e.g., pregnancy safety, liver alerts) in plain English and Urdu.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a fast barcode scanner, DRAP registration lookup, generic mapping database, and offline pricing limits.

### A. Scanning & Verification Engine
*   **Barcode / QR Scanner**: Scan standard product barcodes (UPC/EAN) or 2D matrix codes printed on packaging, blister packs, and syrup bottles.
*   **Manual DRAP ID Input**: Option to search by typing the brand name or the 5/6-digit DRAP Registration Number.
*   **Official Price Inspector**: Displays the regulated MRP. Calculates price-per-unit (e.g., cost per single tablet) so consumers can buy partial blister packs without being overcharged.

### B. Generic Alternator Directory
*   **Active Formula Mapping**: Automatically displays alternative local brands containing the exact same generic active ingredient (API), strength, and dosage form (e.g., entering "Augmentin 375mg Tablet" suggests identical substitutes like "Amoxi-Clav" or "Co-Amoxiclav" of same specs).
*   **Alternative Pricing comparison**: Sorts generic alternatives by price, allowing users to find more affordable options.

### C. Bilingual UI & Offline Mode
*   **Urdu & English Interface**: Native translation toggle for broader accessibility.
*   **Offline Room DB Database**: Caches the top 10,000+ registered drug brands in Pakistan locally, allowing users to search formulas and check official prices inside hospital basements or remote areas with no internet connection.

---

## 3. Phase 2: Advanced Growth Features
For the scale-up phase, the app integrates AI OCR, crowdsourced reporting, live stock trackers, and voice dosage readers.

### A. AI-Powered Doctor Prescription Scanner
*   **Handwriting Deciphering OCR**: Integrates an AI/LLM-based scanner designed to read famously illegible doctor prescriptions in Pakistan. It extracts the recommended medicines, checks their spelling against the database, and adds them directly to the user's checklist.

### B. In-App Price Gouging & Counterfeit Reporting
*   **Receipt Upload & DRAP Alert**: Allows users to take photos of pharmacy receipts and packages to report retail overcharging or suspected counterfeit medicine directly to the DRAP portal and provincial drug inspectors.
*   **Crowdsourced Red-Flags**: Flags pharmacies on the map that have been repeatedly reported by users for selling above MRP.

### C. Live Stock & Shortage Tracker
*   **Local Chain Availability**: Integrates API feeds and crowdsourced stock indicators from major Pakistani pharmacy chains (e.g., Servaid, Fazal Din, DVAGO, D-Watson, Shaheen) to show users where hard-to-find medicines are currently in stock.

### D. Bilingual Voice-Activated Dosage Reader
*   **Audio Dosage Assistant**: A text-to-speech audio reader in Urdu and regional languages describing exact dosage instructions (e.g., *"Yeh goli khane ke baad din mein do dafa lein"*) for elderly or illiterate users.

---

## 4. Backend & Database Specification
*   **Local Database**: Room DB storing the core offline registry (top 10,000+ brands, APIs, and prices).
*   **Scraper Engine**: Python-based scraper running scheduled crawls on DRAP official registration databases to fetch and sync updated MRP pricing slabs.
*   **Data Minimization**: High compression rates for the local database file (under 8MB) to facilitate easy download over metered mobile connections.
