# AllergyGuard (الرجی گارڈ) — Pakistan Allergen Verifier Spec

## Executive Overview & Vision
**AllergyGuard (الرجی گارڈ)** is a real-time, camera-enabled ingredient OCR scanner, barcode lookup, and allergen safety mapping mobile application designed specifically for Pakistani families and individuals managing food allergies and intolerances.

Food and pharmaceutical packaging in Pakistan rarely follows international allergen labeling standards. Major allergens (e.g., milk, eggs, peanuts, soy, wheat/gluten, tree nuts, fish, shellfish, sesame) are frequently hidden in fine-print ingredient lists without distinct bolding or "Contains..." warning summaries. Furthermore, the vast majority of locally manufactured Pakistani food brands (e.g., local bakery items, spices, snacks) are completely missing from global barcode databases like Open Food Facts, causing standard barcode scanners to fail.

AllergyGuard solves this by providing a dual-mode scanning interface: a fast barcode lookup backed by a camera-based ingredient list OCR scanner. Powered by Vision AI (Gemini), the app extracts, translates, and analyzes ingredient lists in real time in both English and Urdu (including Roman-Urdu) to protect users from dangerous exposures.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific labeling and supply chain characteristics of the Pakistani market:
*   **Dual-Mode Scanner (Camera OCR Fallback)**: If a barcode lookup fails (which is common for local Pakistani brands), the app falls back to camera OCR. The user takes a picture of the ingredient list, and the Vision AI extracts and parses the text.
*   **Urdu & Local Term Mapping**: The ingredient database maps local Urdu terms to their master allergens (e.g., *Maida* / *Suji* / *Gandum* map to Wheat/Gluten; *Khoya* / *Mawa* / *Butter* / *Paneer* map to Milk; *Anda* maps to Egg; *Moongphali* maps to Peanut).
*   **Custom Severity Toggles**: Set sensitivity levels per allergen:
    *   *Severe / Anaphylactic*: Zero-tolerance filter. Flags direct ingredients, hidden synonyms, derivatives, and precautionary warnings (e.g., *"May contain traces of..."* or *"Processed in a facility that also handles..."*).
    *   *Intolerance / Sensitivity*: Flags direct ingredients and known chemical derivatives only, ignoring facility trace warnings.
*   **4-Tier Color-Coded Safety Classification**:
    *   **Safe (Green)**: Free of all profile allergens and facility warnings.
    *   **Caution / Traces (Yellow)**: Contains no direct allergens, but carries facility cross-contamination or "may contain" warnings.
    *   **Unsafe (Red)**: Contains one or more profile allergens in direct ingredients or derivatives.
    *   **Unknown (Gray)**: Insufficient ingredient data; manual parent review required.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers dual-mode scanning, basic allergen profile toggles, chemical synonym mapping, and offline caching.

### A. Core Scanning & Data Extraction
*   **Barcode Lookup**: Instantly scan standard EAN/UPC barcodes. Connects to Open Food Facts and a localized database of common Pakistani grocery products.
*   **Camera OCR (Gemini Integration)**: For unregistered local products, the user captures a photo of the ingredient list. Gemini Vision OCR extracts the text, translates Urdu/Roman-Urdu words, and checks them against the active allergen dictionary.

### B. Intelligence & Profile Customization
*   **AI Synonym & Derivative Mapping**: Automatically cross-references ingredients against an active allergen dictionary (e.g., identifying casein, whey, or lactoglobulin as Milk; albumin as Egg; arachis oil as Peanut; soy lecithin as Soy).
*   **Allergen Profile Toggles**: Customize profile for the top allergens: Peanuts, Tree Nuts, Milk, Eggs, Wheat/Gluten, Soy, Fish, Crustacean Shellfish, and Sesame. Users can add custom text filters (e.g., *“Sulfites”*, *“Tartrazine”*).
*   **Bilingual System UI**: Native interface support for English and Urdu (Nastaliq script).
*   **Offline Room DB Database**: Caches E-number classifications, allergen synonyms, and saved product safety logs for offline grocery shopping.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces local Pakistani alternatives, E-number Halal/Allergen mapping, crowdsourced product registration, and emergency anaphylaxis rescue alerts.

### A. Local Pakistani Safe Alternatives
*   **Allergen-Free Brand Suggestions**: When a scanned local item is classified as Unsafe or Caution, the app automatically suggests 2-3 verified safe local alternatives (e.g., suggesting local gluten-free flour brands or dairy-free alternative milks available in Pakistan).

### B. E-Number Halal & Allergen Mapping
*   **Additive Analyzer**: Analyzes E-numbers for both allergen derivatives (e.g., E322 soy lecithin) and optional Halal/Haram status (e.g., animal-derived emulsifiers), integrating dietary checking into a single scan.

### C. Crowdsourced Product Registry
*   **Parent-Driven Database**: Allows parents to submit photos of new local Pakistani grocery items, ingredients, and barcodes to expand the shared local product directory.

### D. Emergency Anaphylaxis & First-Aid Guide
*   **Emergency Mode**: One-tap panic button that dials Rescue 1122 or local emergency contacts.
*   **Visual First-Aid Instructions**: Displays simple, animated, step-by-step instructions in Urdu and English on how to handle an allergic reaction and administer an epinephrine auto-injector (EpiPen).

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing product barcodes and verified ingredient lists, synced to the client Room DB SQLite cache.
*   **Image Processing API**: FastAPI (Python) gateway that pre-processes captured label images (contrast adjustment, cropping) before passing them to the Gemini API for ingredient extraction.
*   **Privacy Engine**: All user allergen profiles and search histories are stored strictly on-device (Room DB). No personal medical data is uploaded to the cloud.