# CardPerks (کارڈ پرکس) — Pakistan Credit Card Discounts Spec

## Executive Overview & Vision
**CardPerks (کارڈ پرکس)** is an independent, location-based credit and debit card discount discovery, automated bank promotion scraper, and card-payment tax optimization mobile application designed specifically for consumers in Pakistan.

Major commercial banks in Pakistan (including HBL, Bank Alfalah, UBL, Meezan Bank, MCB, Allied Bank, Faysal Bank, Silkbank, and Standard Chartered) run aggressive discount campaigns (ranging from 10% to 50% off) across restaurants, supermarkets (Imtiaz, Metro, Carrefour), fashion retailers (Khaadi, Sapphire, J., Gul Ahmed), online portals (Daraz, Foodpanda), and cinemas.

However, finding these discounts at the point of purchase is highly inefficient:
*   **The PDF & SMS Nightmare**: Banks publish their promotions in massive, disorganized PDF files buried on their websites or blast them via temporary SMS notifications.
*   **Card Tier Complexity**: Discounts differ depending on the card brand (Visa, Mastercard, UnionPay, PayPak) and specific tier (Classic, Gold, Platinum, Signature, Infinite, World, World Elite).
*   **Delayed Awareness**: At the retail check-out counter, customers frequently ask: *“Is any card discount available here?”* — only to find out too late, resulting in lost savings.

CardPerks solves these pain points by offering a location-based mobile app that securely maps a user's wallet cards to nearby merchants in real time, ensuring they never miss a deal without storing sensitive financial data.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific characteristics of the Pakistani retail banking and retail market:
*   **Non-Sensitive Card Vault**: Users select their cards by issuing bank and network tier (e.g., *“Bank Alfalah Visa Platinum”*, *“HBL World Mastercard”*, *“Meezan Bank PayPak Gold”*). The app stores zero card numbers, CVVs, or expiration dates, bypassing regulatory/compliance barriers (State Bank of Pakistan guidelines).
*   **Location-Based Merchant Matching**: Displays nearby restaurants and retail outlets, sorting them by the highest discount percentage available in the user's custom wallet.
*   **Provincial Restaurant Card-Tax Benefit**: Automatically reminds users of lower sales tax rates mandated by provincial revenue authorities (PRA in Punjab, SRB in Sindh) when paying via credit/debit card at restaurants (e.g., 5% card payment tax vs. standard 16% cash tax).
*   **Automated Bank Scrapers**: Backend scrapers crawling PDF and HTML promotion tables across HBL, Alfalah, UBL, and Meezan Bank pages to update the index weekly.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a non-sensitive card vault, location-based discount matching, a bilingual interface, and offline caching.

### A. Core Directories & Matching
*   **Non-Sensitive Card Vault**: A simple checkbox checklist where users build their virtual wallet by selecting their bank and card network tier.
*   **Location-Based Deal Finder**: Integrates user coordinates with nearby merchant branches to show active card discounts (e.g., *"Kolachi Restaurant: 30% off using your UBL Mastercard Platinum"*).
*   **Category Filters**: Filter deals by Food & Dining, Supermarkets, Apparel & Shopping, and Fuel.

### B. Mobile UI & Caching
*   **Bilingual Nastaliq UI**: Complete Urdu and English toggle using native Nastaliq font styles.
*   **Offline Cache (Room DB)**: Caches local merchant lists and active discounts, allowing users to consult deals inside shopping malls with poor cellular coverage.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces automated bank portal scrapers, geo-proximity notifications, restaurant card tax calculators, and crowdsourced POS deal verifiers.

### A. Automated Bank Portal Scraper Backend
*   **Weekly Scraper Worker**: Python-based scraper crawling major commercial bank promotions pages, extracting rates, merchant branches, card validity ranges, and converting them to structured database rows.

### B. Geo-Proximity Push Notifications
*   **Proximity Alerts**: Sends geofenced push alerts (using H3 Resolution 8 spatial cells) when the user walks within 100 meters of a merchant running a major (>30%) discount on one of their saved cards.

### C. Restaurant Card-Tax Auditor
*   **Card Payment Tax Checker**: In-app calculator checking if the restaurant POS applied the legal card discount rate (5%) instead of the higher cash rate, and checks for GST transparency.

### D. Crowdsourced POS Deal Verifier
*   **Receipt Verification Log**: Allows users to take photos of receipts and flag merchants who refuse card discounts, fail to apply advertised bank partnerships, or claim the deal has expired.