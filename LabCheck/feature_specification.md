# LabCheck (لیب چیک) — Pakistan Diagnostic Lab Auditor Spec

## Executive Overview & Vision
**LabCheck (لیب چیک)** is an independent, crowdsourced diagnostic price directory, regulatory compliance tracker, and medical bill auditor mobile application designed specifically for patients in Pakistan.

The diagnostic laboratory sector in Pakistan is highly fragmented and poorly regulated. Patients face major transparency and safety challenges:
*   **Massive Price Discrepancies**: The cost of standard diagnostic tests (e.g., Complete Blood Count (CBC), Liver Function Tests (LFTs), Lipid Profile, PCR, Thyroid profile) varies wildly across different diagnostic chains, with prices for the same test ranging from Rs. 800 to Rs. 4,000.
*   **Unlicensed Collection Centers**: Dozens of small, local blood collection points operate without valid licenses from provincial regulators, often utilizing poorly calibrated machines or lacking qualified pathologists, which leads to faulty diagnostic results.
*   **Doctor Kickbacks**: A widespread, unethical industry practice involves diagnostic chains paying significant commissions/kickbacks (ranging from 20% to 50%) to prescribing doctors, driving up the baseline cost of medical tests for self-paying patients.

LabCheck solves these issues by offering a test price comparison index, provincial regulatory license lookup directories, and crowdsourced bill audits.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific patterns of the Pakistani healthcare retail system:
*   **National Price Comparison Index**: Compares pricing of common tests across major national diagnostic chains, including:
    *   Aga Khan University Hospital (AKUH) Labs
    *   Chughtai Lab
    *   Islamabad Diagnostic Center (IDC)
    *   Al-Khidmat Labs (Welfare)
    *   Shaukat Khanum Memorial Hospital Labs
*   **Regulatory Commission Lookup**: Cross-references laboratories and collection points with provincial healthcare regulatory bodies to verify active registration status:
    *   PHC (Punjab Healthcare Commission)
    *   SHCC (Sindh Healthcare Commission)
    *   KP HCC (Khyber Pakhtunkhwa Health Care Commission)
    *   BHC (Balochistan Healthcare Commission)
*   **Direct-to-Patient Discount Tracking**: Highlights independent and welfare labs (like Al-Khidmat) that refuse to pay doctor commissions and instead pass flat 30%-50% discounts directly to walk-in, self-paying patients.
*   **Urdu & English Reference Guides**: Plain explanations of common test reference ranges in Urdu and English.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a bilingual test price comparison directory, regulatory license lookup directory, home sample fee index, and offline caching.

### A. Core Directories & Verification
*   **Diagnostic Price comparison**: Search and compare rates of the top 50 most common diagnostic tests and profiles across the major national lab networks.
*   **License & Registration Lookup**: Search collection centers and labs by city, sector, and registration number to verify active PHC, SHCC, or KP HCC licenses.
*   **Home Sampling Comparator**: Compare home sample collection fees, active service coverage boundaries, booking numbers, and turnaround times (TAT).

### B. Mobile UX & Bilingual Support
*   **Urdu & English Interface**: Complete native toggle support between English and Urdu (Nastaliq script).
*   **Offline Cache (Room DB)**: Caches searched test prices, nearby licensed collection centers, and basic reference ranges locally, allowing patients to consult guides inside hospital basements with poor signal.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces AI-powered bill and report audits, doctor commission trackers, and crowdsourced collection center safety reviews.

### A. AI-Powered Bill & Report Auditor
*   **Camera Bill Scanner**: Users capture photos of laboratory bills. Vision AI (Gemini) extracts test names, compares them against average market rates and official guidelines, and highlights any overcharging or hidden service markups.
*   **Lab Report Interpreter**: Users scan their diagnostic reports. The AI translates clinical jargon into simple, plain English and Urdu (e.g., explaining what high cholesterol or low hemoglobin means in a friendly, conversational tone).

### B. Anti-Commission Direct Discount Locator
*   **Ethical Lab Directory**: Maps and highlights laboratories that bypass doctor commissions to offer direct cash discounts (30% to 50%) to self-paying patients.
*   **Commission Reporting**: An anonymous submission box where patients and lab staff can report clinics or doctors demanding kickbacks.

### C. Crowdsourced Quality & Hygiene Audits
*   **Collection Point Reviews**: Allows patients to rate collection centers on critical parameters: hygiene, syringe disposal practices (disposable needle validation), staff phlebotomy skill (pain levels), and turnaround time (report delays).

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing verified master price lists, district-wide home sampling rates, and healthcare commission registries, synced to the client Room DB SQLite cache.
*   **Scraper Worker**: Python-based scraper crawling savings/price lists and provincial commission databases.
*   **On-Device Security**: All scanned bill files and medical report details are processed on the backend and immediately destroyed to protect patient health confidentiality.