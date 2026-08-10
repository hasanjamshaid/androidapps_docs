# AllergenCheck — Global Expected Revenue Model & Projections

This document outlines the expected revenue model, monetization channels, target customer segments, and financial scenarios for **AllergenCheck**, the mobile ingredient OCR scanner, barcode lookup, and allergen safety mapping app for global markets (US, UK, and European Union).

---

## 1. Target Customer Segments & Global Context

In high-purchasing-power digital economies (US/UK/EU), food allergies and intolerances affect over 250 million people, and food safety standards require daily vigilance. AllergenCheck addresses this through a dual-mode camera OCR and barcode scanner, delivering real-time ingredient analysis.

*   **Primary Audience**:
    *   Families managing severe, anaphylactic food allergies (peanuts, eggs, dairy, shellfish).
    *   Individuals with common food intolerances (celiac disease/gluten sensitivity, lactose intolerance).
    *   Health-conscious shoppers verifying pharmaceutical and cosmetic ingredients for harmful chemicals or animal derivatives.
*   **Ad-First Strategy**: The application is positioned as an ads-primary free utility. The free tier contains display ads, generating substantial revenue from high-value Western digital ad economies (high AdMob CPMs). An ad-free experience is reserved for premium Pro subscribers.

---

## 2. Monetization Vectors

AllergenCheck monetizes through free tier display ads, premium B2C subscriptions (AllergenCheck Pro), B2B brand placements, and global affiliate e-commerce commissions.

```mermaid
graph TD
    User([App User]) -->|Free Scanner Use| Free[Free Tier]
    User -->|Unlock Pro Tier| Pro[2. AllergenCheck Pro Subscription]
    Free -->|Display Ad Impressions| Ads[1. Contextual Display Ads]
    User -->|Browse Safe Brands| Brand[3. B2B Alternative Placements]
    User -->|Shop Organic Groceries| Shop[4. E-Commerce Affiliate Store]

    Ads -->|Western AdMob CPMs ($3.50)| Rev[Total App Revenue (USD)]
    Pro -->|$1.99/mo subscription (Ad-Free)| Rev
    Brand -->|$100/mo sponsorship spot| Rev
    Shop -->|5% affiliate commission| Rev
```

### A. Contextual Display Ads (Primary Stream)
*   **Format**: Non-intrusive banner ads displayed on product logs and safety scorecards for free users.
*   **Monetization Mechanism**: CPM-based AdMob / digital ad networks.
*   **Western Ad CPM**: **$3.50 USD** average across US/UK/EU.
*   **Engagement**: Free tier users average 8 check-in sessions/month, viewing 6 pages/session (48 ad impressions/month).

### B. AllergenCheck Pro (Premium B2C Subscriptions)
*   **Format**: Premium subscription unlocking advanced features and removing all ads.
*   **Pro Features**:
    *   Unlimited Gemini Vision OCR scans (free tier limited to 5 scans/month).
    *   Advanced pharmaceutical, supplement, and cosmetic ingredient audits.
    *   Offline Room database dictionary updates.
*   **Pricing**: **$1.99 USD / month** or **$12.99 USD / year**.
*   **Conversion Rate**: Projected at **1.5% of MAU** (2.0% in Optimistic scenario).

### C. Allergen-Free B2B Brand Placements
*   **Format**: When a user scans an "unsafe" product (e.g. wheat-based flour), partner brands paying a monthly sponsorship spot display verified safe alternatives (e.g. gluten-free flour brands).
*   **Pricing**: **$100 USD / month** per brand sponsor.
*   **Conversion Rate**: Projected at 10 active sponsors in Year 1.

### D. E-Commerce Affiliate Store Commissions
*   **Format**: Marketplace in the app recommending organic or allergen-free grocery bundles, linking to global stores (e.g., Amazon, iHerb).
*   **Average Basket Size**: **$40 USD**.
*   **Affiliate Commission**: **5% of basket** ($2.00 USD net commission).
*   **Conversion Rate**: Projected at **0.50% of MAU** purchasing monthly.

---

## 3. Financial Projections (Year 1)

These projections are based on three scenarios of **Monthly Active Users (MAU)** reached by Month 12.
*(Exchange rate used: 1 USD = 278 PKR)*

### Scenario Comparison Table

| Metric | Scenario A (Conservative) | Scenario B (Base Case) | Scenario C (Optimistic) |
| :--- | :--- | :--- | :--- |
| **Year 1 Target MAU** | 15,000 | 50,000 | 150,000 |
| **Pro Subscribers (1.0% - 2.0%)**| 150 (1.0%) | 750 (1.5%) | 3,000 (2.0%) |
| **Monthly Affiliate Sales (0.3% - 0.7%)**| 45 sales (0.30%) | 250 sales (0.50%) | 1,050 sales (0.70%) |
| **B2B Sponsor Partners** | 3 | 10 | 25 |
| **Ad CPM (USD)** | $3.00 | $3.50 | $4.00 |
| **Monthly Sessions per User** | 6 | 8 | 12 |
| **Views per Session** | 4 | 6 | 8 |
| **Monthly Ad Revenue** | **$1,069.20** (297,238 PKR) | **$8,274.00** (2,300,172 PKR) | **$56,448.00** (15,692,544 PKR) |
| **Monthly Affiliate Comm**| $67.50 (18,765 PKR) | $500.00 (139,000 PKR) | $2,625.00 (729,750 PKR) |
| **Monthly B2B Placement Rev** | $150.00 (41,700 PKR) | $1,000.00 (278,000 PKR) | $5,000.00 (1,390,000 PKR) |
| **Monthly Pro Subscription Rev** | $298.50 (82,983 PKR) | $1,492.50 (414,915 PKR) | $5,970.00 (1,659,660 PKR) |
| **Total Expected MRR (USD)** | **$1,585.20** | **$11,266.50** | **$70,043.00** |
| **Total Expected MRR (PKR equivalent)** | **440,686 PKR** | **3,132,087 PKR** | **19,471,954 PKR** |
| **Total Projected ARR (USD)** | **$19,022.40** | **$135,198.00** | **$840,516.00** |
| **Total Projected ARR (PKR equivalent)** | **5,288,227 PKR** | **37,585,044 PKR** | **233,663,448 PKR** |

---

## 4. Key Financial Formulas

$$\text{Total Monthly Revenue (USD)} = R_{ad} + R_{subs} + R_{referrals} + R_{placements}$$

Where:

1.  **Contextual Ad Revenue ($R_{ad}$)**:
    $$R_{ad} = \text{MAU} \times (1 - \text{ProConv}) \times \text{Sessions} \times \text{ViewsPerSession} \times \frac{\text{CPM}_{USD}}{1000}$$
2.  **Premium Pro Subscriptions ($R_{subs}$)**:
    $$R_{subs} = \text{MAU} \times \text{ProConv} \times \text{Price}_{USD}$$
3.  **Affiliate Store Commissions ($R_{referrals}$)**:
    $$R_{referrals} = \text{MAU} \times \text{SalesRate} \times \text{Basket}_{USD} \times \text{CommRate}$$
4.  **B2B Alternative Placements ($R_{placements}$)**:
    $$R_{placements} = \text{PartnerCount} \times \text{MonthlySponsorFee}_{USD}$$

---

## 5. Dynamic Revenue Calculator

To modify these variables, run custom scenarios, or perform real-time sensitivity analysis, open the interactive browser-based dashboard calculator:

👉 **[revenue_calculator.html](file:///c:/Essentials/SmartFarms/androidapps_docs/revenue_calculator.html)**

*Open the file in any web browser to adjust parameters (e.g. MAU size, shopping affiliate conversion, sponsor count) and view updated revenue breakdowns instantly in USD.*
