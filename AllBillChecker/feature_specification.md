# All Bill Checker Pakistan — Android App Specification

## Executive Overview & Vision
**All Bill Checker Pakistan** is a unified utility management and billing intelligence mobile application designed specifically for Pakistani consumers. 

Utility billing in Pakistan is complex, fragmented, and volatile. Customers face frequent tariff changes, fuel price adjustments (FPA), and strict consumption "slabs" where crossing a single unit threshold can double or triple the total bill. Additionally, checking bills online requires navigating slow, outdated government DISCO/SNGPL/WASA web portals, many of which are protected by frustrating Captchas.

This app solves these pain points by offering a single-point hub to fetch, monitor, archive, and analyze electricity, gas, and water bills. Users can manage multiple properties, calculate future bills based on active meter readings, and receive smart reminders to keep their bills low.

---

## 1. Provider Integrations
The app integrates with all major utility service providers across Pakistan:

*   **Electricity (DISCOs & KE)**:
    *   **All Government DISCOs**: LESCO (Lahore), IESCO (Islamabad/Rawalpindi), MEPCO (Multan), FESCO (Faisalabad), GEPCO (Gujranwala), PESCO (Peshawar), HESCO (Hyderabad), SEPCO (Sukkur), QESCO (Quetta), and TESCO (Tribal areas).
    *   **K-Electric (KE)**: Serving Karachi consumers via Account/Consumer Number.
*   **Sui Gas**:
    *   **SNGPL** (Sui Northern Gas Pipelines Limited): Serving Punjab, KP, and Islamabad.
    *   **SSGC** (Sui Southern Gas Company): Serving Sindh and Balochistan.
*   **Municipal Water (WASA & KWSB)**:
    *   **WASAs**: Lahore, Rawalpindi, Faisalabad, Hyderabad, Multan, and Gujranwala.
    *   **KWSB** (Karachi Water & Sewerage Board) & **CDA** (Capital Development Authority, Islamabad).

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on providing a fast, reliable tool for checking, downloading, and storing utility bills with zero account creation required.

### A. Core Discovery & Utility Management
*   **Property & Account Manager**: Save multiple utility reference numbers under custom nicknames (e.g., "Home Electricity", "Shop Gas", "Saeed's Rent WASA").
*   **One-Tap Refresh**: A dashboard action that queries all saved bills sequentially and flags which bills are new or unpaid.
*   **Bilingual Interface (Urdu & English)**: Complete native toggle between English and Urdu (اردو) for wider accessibility across demographics.
*   **Offline Access**: Caches the last successfully fetched bills locally in a Room database, allowing users to view duplicate bills without an active internet connection.

### B. Bill Fetching & Captcha Fallback
*   **Direct Portal Scraping**: Fetches bill data directly from official public portals (PITC, K-Electric, SNGPL, SSGC) via secure backend HTTP endpoints.
*   **Bypass / Intercept WebView**: For portals that enforce Captchas (e.g., K-Electric or SSGC), the MVP displays a clean in-app pop-up showing only the Captcha image, allowing the user to solve it. The solved token is then sent to the scraper to finalize the fetch.
*   **PDF Generation & Export**: Renders high-resolution duplicate bills accepted at bank counters, post offices, and retail agent shops (EasyPaisa/JazzCash). Supports direct printing and sharing via WhatsApp/Email.

### C. Basic Value-Added Tools
*   **Simple Bill Calculator**: Input current meter reading to calculate estimated electricity usage against last month's final reading.
*   **Tariff Slab Guide**: Reference sheet displaying current NEPRA slab rates, duties, taxes, and estimated FPA (Fuel Price Adjustments).

---

## 3. Phase 2: Advanced Growth Features
Once the MVP is launched and validated by high user hit rates, the application will be updated with advanced automation, payment integrations, and AI analytics.

### A. Automated OCR Captcha Solver
*   **Background ML Resolver**: Integrates a lightweight neural network (such as CNN-based OCR) on the backend server that automatically parses and solves simple numeric or text captchas from utility sites.
*   **Silent Background Checks**: Allows the app to run scheduled checks in the background (e.g., at 3:00 AM) to detect new bills without requiring any user interaction.

### B. NEPRA "Protected Status" Tracker & Slab Alerts
*   **Protected Status Guard**: In Pakistan, residential electricity consumers using under 200 units monthly for 6 consecutive months receive "Protected" status, which has significantly lower baseline tariffs. The app tracks unit history and alerts the user: 
    > [!WARNING]
    > *You have used 182 units this month. If you consume less than 18 units in the next 6 days, you will retain your **Protected Consumer** tariff status and save up to 4,000 PKR.*
*   **Peak/Off-Peak Shift Alerts**: Reminders for time-of-use (three-phase) meter users to shift heavy loads (ACs, water pumps) out of peak hours (typically 6:00 PM to 10:00 PM).

### C. Tax Certificate & Document Downloader
*   **Income Tax Certificates**: Allows active tax filers to fetch and download Annual Withholding Tax Certificates (under Section 235/236) directly through their consumer numbers for tax filing purposes.

### D. Smart Solar ROI & Energy Advisor
*   **Net-Metering Analytics**: Tracks export vs. import credits for net-metered solar homes.
*   **Solar Feasibility Calculator**: Input average monthly unit consumption to calculate recommended solar array size (3kW, 5kW, 10kW, etc.), battery capacity (Ah) for UPS backups, and estimated payback period (ROI).

### E. Deep-Link Payments & Verification
*   **Mobile Wallet Deep Linking**: Pre-fills reference numbers and redirects users to EasyPaisa, JazzCash, or Nayapay apps for payment.
*   **Payment Status Scanner**: Uses the device camera to scan utility barcodes, querying official records to verify if the payment has successfully cleared at the bank.

---

### Backend Scraping & Security
*   **Scraper Worker**: Written in Python using optimized requests sessions and HTTP client pools to fetch bill HTML structures.
*   **Session Management**: Keeps track of active cookies to bypass redundant captcha requests during multi-property dashboard refreshes.
*   **Privacy First**: No consumer names, CNIC, or geographic coordinates are stored on the server. All Reference Numbers and historical unit records are cached strictly on the client's local SQLite database (Room DB).