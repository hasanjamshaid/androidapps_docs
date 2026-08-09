# KismatBond (قسمت بانڈ) — Pakistan Prize Bond Scanner Spec

## Executive Overview & Vision
**KismatBond (قسمت بانڈ)** is a camera-enabled prize bond OCR scanner, portfolio management, and draw tracking mobile application designed specifically for Pakistani savers and investors.

National Savings prize bonds (offered in denominations of Rs. 100, 200, 750, 1,500, and registered Premium bonds of Rs. 25,000 and 40,000) are a highly popular, interest-free investment vehicle in Pakistan. However, tracking draws is a massive administrative headache:
*   **Tedious Manual Verification**: Checking drawers requires manually searching through slow, large official text files or PDFs published by National Savings Pakistan. Matching hundreds of physical bonds is highly error-prone.
*   **6-Year Expiry Limit**: Many winners remain unaware they have won a prize, and the claim expires exactly 6 years from the draw date, resulting in millions of unclaimed rupees.
*   **Filer vs. Non-Filer WHT Complexity**: Net payouts vary drastically based on FBR (Federal Board of Revenue) active taxpayer status, with withholding tax (WHT) rates doubling for non-filers.

KismatBond solves these problems by providing localized mobile camera OCR scanning, automated series generation, backend draw scraper integration, FBR tax calculators, and claim form assistants.

---

## 1. Targeted Local Context & Critical Metrics
The app is tailored to the specific characteristics of the Pakistani National Savings system:
*   **Optimized 6-Digit OCR Reader**: Mobile camera reader calibrated to read the unique font and serial placement of physical Pakistani bearer bonds, reducing scan errors.
*   **Filer vs. Non-Filer Tax Calculator**: Computes actual net winnings by applying the current FBR withholding tax (WHT) rates (15% for Active Taxpayers/Filers vs. 30% for Non-Filers).
*   **Premium registered Bonds Manager**: Specific profiles to track registered Premium bonds (Rs. 25,000 & Rs. 40,000) which pay bi-annual profit directly to bank accounts and have draws linked to CNICs.
*   **6-Year Expiry Countdown**: Tracks draw dates and displays warning countdowns before a prize-winning bond hits the legal 6-year claim limit.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on delivering physical bond OCR scanning, portfolio organization, and automated draw matching from scraped official files.

### A. Scanning & Entry Engine
*   **Camera OCR Scanner**: Localized mobile scanner that parses the 6-digit serial number, denomination, and series prefix directly from the paper bond.
*   **Batch & Series Entry**: Allows users to enter continuous series ranges in seconds (e.g., entering prefix/suffix and ranges like *“123401 to 123500”*), generating the full list automatically.

### B. Portfolio & Draw Matching
*   **Virtual Lockers**: Organize saved bonds under profiles (e.g., "Personal Vault", "Father's Bonds", "Business Holdings").
*   **Automated Match Scraper**: Backend scheduler that crawls National Savings Pakistan publications, matches saved numbers, and alerts wins.
*   **Offline Draw Database (Room DB)**: Stores the past 10 years of draw results locally, allowing users to run historical checks on old bonds without requiring internet.
*   **Bilingual Interface (Urdu & English)**: Complete native toggle between English and Urdu.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app integrates FBR active taxpayer lookups, Premium registered bond profiles, automated WhatsApp alerts, and claim form generators.

### A. FBR Active Taxpayer List (ATL) Integration
*   **CNIC Status Check**: Allows users to input their CNIC. The app checks FBR's Active Taxpayer List (ATL) to verify Filer status in real time, automatically calculating correct withholding tax deductions on potential winnings.

### B. Premium Prize Bonds Profit Tracker
*   **Registered Bonds Ledger**: Logs CNIC, Bank Account Details (IBAN), and Registration Receipts for Premium Bonds.
*   **Bi-Annual Profit Alarms**: Calculates and alerts users when bi-annual profit distributions (e.g., 25,000 and 40,000 premium bonds) are scheduled to be deposited directly into their bank accounts.

### C. WhatsApp & SMS Win Alerts
*   **Real-Time Push Alerts**: Sends high-priority push notifications, SMS, or WhatsApp alerts the instant a new draw is published and a match is found in the user’s lockers.

### D. SBP & National Savings Claim Form Generator
*   **Form Pre-Filler Assistant**: Pre-fills the official claim application forms (such as Form 22 or DR-1) required to submit at State Bank of Pakistan (SBP) offices or National Savings Centers. It outputs a print-ready PDF containing the owner's CNIC, bank IBAN, and the winning bond serial details.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing verified master draw lists, synced to the client Room DB SQLite database for offline querying.
*   **Scraper Worker**: Python-based scraper crawling savings.gov.pk daily for new draw PDFs and text lists, converting them into structured database rows.
*   **On-Device Security**: All scanned prize bond serial numbers are stored locally on the device (Room DB) to protect investor privacy. Cloud syncing is encrypted and optional.