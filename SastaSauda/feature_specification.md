# SastaSauda (سستا سودا) — Pakistan Supermarket Basket Price Auditor Spec

## Executive Overview & Vision
**SastaSauda (سستا سودا)** is a crowdsourced monthly grocery basket price comparison, FBR receipt OCR auditor, shrinkflation tracker, and bank card discount optimization mobile application designed specifically for consumers in Pakistan.

Double-digit inflation in Pakistan has made monthly grocery shopping a source of high financial stress. Major local and multinational supermarket chains charge widely varying prices for identical branded products:
*   **Pricing Discrepancies**: Staples (e.g., cooking oil/ghee like Dalda, tea like Tapal, milk like Olpers/Nestle Milkpak, flour/atta like Ashrafi/Sunridge, detergent like Surf Excel) vary significantly across discount networks (e.g., Imtiaz Super Market, Chase Up, Save Mart) compared to premium or wholesale chains (e.g., Metro Cash & Carry, Carrefour, Alfatah, Jalal Sons).
*   **Shrinkflation Tactics**: Brands frequently reduce packaging sizes (e.g., shrinking a tea pack from 950g to 800g, or a soap bar from 150g to 115g) while keeping the retail price unchanged, effectively raising the price-per-gram.
*   **Complex Credit Card Promotions**: Supermarkets run rotating bank credit/debit card discounts (e.g., 10% to 15% off on specific days with HBL, Bank Alfalah, Silkbank cards), making it difficult for shoppers to calculate the true cheapest store.

SastaSauda solves these challenges by allowing users to compile a standard monthly grocery list, compare total basket costs side-by-side across major supermarket networks, audit receipts via camera scanning, and optimize card discounts.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific patterns of the Pakistani retail market:
*   **Major Supermarket Networks**: Compares grocery prices across leading chains in major cities:
    *   Imtiaz Super Market
    *   Metro Cash & Carry
    *   Carrefour
    *   Alfatah Super Market
    *   Chase Up
    *   Save Mart (Islamabad/Rawalpindi)
*   **FBR POS Receipt Scanning**: In Pakistan, large marts issue thermal receipts connected to FBR (Federal Board of Revenue) point-of-sale systems. The app utilizes camera OCR to scan these slips, automatically updating the crowdsourced price index.
*   **Shrinkflation Metrics**: Calculates cost-per-gram shifts to reveal when package sizing drops are used to mask inflation.
*   **Bank Card & Loyalty Discount Optimization**: Maps rotating bank card deals to calculate net basket costs, advising the shopper which card from their wallet to use at checkout.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a monthly basket comparison planner, a camera receipt OCR scanner, a bilingual interface, and offline caching.

### A. Core Comparison & Scanning
*   **Monthly Basket Price Index**: Compile a monthly list of standard grocery staples (flour, oil, sugar, tea, milk, laundry detergent). The app calculates and compares the total checkout cost side-by-side across Metro, Carrefour, Imtiaz, Alfatah, Chase Up, and Save Mart in the user's city.
*   **Receipt OCR Price Extractor**: Users take photos of paper receipts. The AI OCR (Gemini) extracts product names, unit weights, and prices, instantly updating the shared community database.

### B. Mobile UI & Caching
*   **Bilingual Nastaliq UI**: Toggle between English and Urdu using native Nastaliq font styles.
*   **Offline Cache (Room DB)**: Caches recently evaluated basket prices, favorite grocery lists, and standard item rates locally for offline lookup inside supermarkets.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces shrinkflation alerts, card discount calculators, deal verifiers, and nearest store mapping.

### A. Shrinkflation Alert Registry
*   **Weight Reduction Monitor**: A public log displaying products that have undergone packaging size reductions (e.g., showing a 950g to 800g tea pack shift) and calculates the actual price-per-gram percentage hike.

### B. Bank Card & Loyalty Discount Optimizer
*   **Wallet Optimizer**: Users select which bank credit/debit cards they own (e.g., HBL, Alfalah, UBL, Meezan). The app automatically applies active bank partnerships and loyalty program rules to the monthly basket comparison, showing the true net checkout cost.

### C. Deal Verifier & Receipt GST Auditor
*   **Deal Authenticity Audit**: Scans store promotional tags (e.g., *"Buy 2 Get 1 Free"* or *"Special Family Pack"*) to verify if the unit rate is actually cheaper than competitor standard pricing.
*   **GST Checker**: Audits scanned receipts to verify if sales tax calculations conform to FBR standard rates (identifying tax-exempt essential food items vs. taxable processed goods).

### D. Cheapest Outlet Navigator
*   **Store Locator**: Maps the closest outlets of the cheapest evaluated supermarket chain based on user location coordinates.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing product details, local branch coordinates, and active bank card discount promotions, synced to the client Room DB SQLite cache.
*   **OCR Parsing Gateway**: Python (FastAPI) backend that processes receipt photos, parses line items, and updates the master price index after validating FBR transaction data.
*   **Community Security**: Price edits submitted via receipts undergo automated outlier detection (e.g., flag if a product price deviates >50% from the median city price) before approval.