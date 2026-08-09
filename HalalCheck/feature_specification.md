# HalalCheck (حلال چیک) — Pakistan Halal/Haram Verifier Spec

## Executive Overview & Vision
**HalalCheck (حلال چیک)** is a real-time, camera-enabled ingredient OCR scanner, barcode lookup, and Islamic dietary compliance mobile application designed specifically for Pakistani consumers.

While Pakistan is a Muslim-majority country with state Halal regulations, the market faces unique challenges:
*   **Imported Products**: High-end supermarkets (such as Alfatah, Jalal Sons, Esajee's, Imtiaz) carry a vast array of imported foods, cosmetics, and medicines. These items frequently contain non-halal ingredients like pork-derived gelatin, cochineal/carmine dye (E120), whey processed with animal rennet, or pork fat (tallow/lard) derivatives in soaps and cosmetics.
*   **Jurisprudential Variations (Madhhabs)**: Different Islamic schools of thought (*Madhhabs*) have varying rulings on specific dietary items, such as marine life (e.g., the Hanafi school classifying crabs, lobsters, and prawns as non-permissible/Makruh, whereas Shafi'i/Maliki classify them as Halal), gelatin transformation (*Istihalah*), and alcohol-based extraction thresholds.
*   **Barcode Gaps for Local Brands**: Local packaged goods often lack representation in global product databases, preventing standard barcode scanners from retrieving ingredient details.

HalalCheck solves these issues by combining a dual-mode scanner (barcode lookup + camera OCR) with custom jurisprudential toggles to classify products strictly into Halal, Haram, Mushbooh (Doubtful), or Under Review based on the user's specific school of thought.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific consumption patterns and religious parameters of the Pakistani market:
*   **Madhhab-Specific Toggles**: Hanafi, Shafi'i, Maliki, Hanbali. Toggling these dynamically adjusts the classification engine:
    *   *Hanafi*: Flags non-fish marine life (crabs, lobsters, shrimp/prawns) as Mushbooh or Haram, while other Madhhabs show them as Halal.
    *   *Gelatin & Alcohol Extraction*: Custom preferences to filter bovine/poultry gelatin (requiring Halal Zabiha slaughter) and alcohol extraction levels in flavorings (e.g. vanilla extract) or beverages.
*   **Dual-Mode Scanner (Camera OCR Fallback)**: If a barcode lookup fails, the app uses Camera OCR. The user takes a picture of the ingredient list, and the Vision AI (Gemini) extracts, translates, and analyzes the text.
*   **4-Tier Halal Classification**:
    *   **Halal (Green)**: Permissible under the selected Madhhab and certified by a recognized Halal body.
    *   **Mushbooh / Doubtful (Yellow)**: Contains ingredients (such as animal-derived emulsifiers, whey, or gelatin) where the source (bovine vs. porcine) is not verified.
    *   **Haram (Red)**: Contains prohibited ingredients (pork, lard, alcohol, or non-Zabiha animal derivatives).
    *   **Under Review / Unknown (Gray)**: Incomplete data; requires manual review.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers dual-mode scanning, basic Madhhab-specific profile toggles, E-number dictionary lookup, and offline caching.

### A. Dual-Mode Scanning & Data Extraction
*   **Barcode Lookup**: Fast scanning of standard UPC/EAN barcodes. Queries global databases (Open Food Facts) and a localized Pakistani grocery product registry.
*   **Camera OCR (Gemini Integration)**: Extracts bilingual (Urdu & English) ingredient list text from packaging photos, translating local Urdu terms (e.g., *Charbi* maps to Fat/Lard, *Sirka* maps to Vinegar).

### B. Intelligence & Profile Customization
*   **Madhhab Jurisprudence Selector**: Quick toggle for Hanafi, Shafi'i, Maliki, and Hanbali preferences.
*   **E-Number Classification Directory**: Displays the permissibility of food additives (E-numbers like E120 Carmine, E441 Gelatin, E471 Emulsifiers) based on common raw material sources.
*   **Bilingual System UI**: Full native UI support for English and Urdu (Nastaliq script).
*   **Offline Room DB Cache**: Stores the E-number lookup registry and cached search results, enabling offline checks inside supermarkets.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app integrates certified Halal alternatives, official regulatory database synchronization, cosmetic/pharmaceutical auditing, and crowdsourced registry building.

### A. Certified Halal Alternatives
*   **Halal Substitution Engine**: When a scanned product is classified as Haram or Mushbooh, the app automatically suggests 2-3 verified Halal-certified local alternatives available in the Pakistani market (e.g., local Halal jelly, local cheese brands using microbial rennet).

### B. Pakistan Halal Authority (PHA) Registry Sync
*   **Official Database Sync**: Cross-references barcodes and brand names against the registries of the Pakistan Halal Authority (PHA) and provincial bodies (Punjab Halal Development Agency - PHDA, Sindh Halal Authority - SHA) to verify active Halal certifications.

### C. Cosmetics & Pharmaceutical Ingredient Audit
*   **Non-Food Auditing**: Expands ingredient checking to personal care items (soaps, lipsticks, toothpastes) and medicines (capsules, syrups), checking for animal fats, collagen, glycerin, and non-slaughtered gelatin.

### D. Crowdsourced Product Registry
*   **Community Submissions**: Allows users to photograph and submit new product barcodes and ingredient lists. Submissions go through an admin review queue before being added to the master directory.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing product barcodes, active Halal certifications, and the E-number master directory, synced to the client Room DB SQLite cache.
*   **Scraper Engine**: Python scraper that crawls international Halal certification bodies and local PHA portals to maintain up-to-date brand compliance lists.
*   **Privacy First**: All user school of thought choices and search histories are saved locally (Room DB) on the device to protect user privacy.