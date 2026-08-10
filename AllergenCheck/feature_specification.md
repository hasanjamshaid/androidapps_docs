# AllergenCheck — Global Allergen Scanner Spec

## Executive Overview & Vision
**AllergenCheck** is a real-time, camera-enabled ingredient OCR scanner, barcode lookup, and allergen safety mapping mobile application designed for families and individuals managing food allergies and intolerances globally.

Food, cosmetics, and pharmaceutical packaging globally often contain complex ingredient lists where allergens or chemical derivatives are hidden or poorly highlighted. For families managing severe, life-threatening food allergies or conditions like celiac disease, scanning labels is a stressful daily necessity. Additionally, many imported or local specialty brands are missing from standard databases, causing basic scanners to fail.

AllergenCheck solves this by providing a dual-mode scanning interface: a fast barcode lookup connected to global database networks (such as Open Food Facts) backed by a high-speed camera OCR scanner. Powered by Gemini Vision AI, the app extracts, translates, and analyzes ingredient lists in real time across multiple languages to protect users from accidental exposure.

---

## 1. Targeted Global Context & Critical Metrics
The app is engineered to address the complexities of global food labeling and cross-border ingredients:
*   **Dual-Mode Scanner (Camera OCR Fallback)**: If a barcode lookup fails (which is common for small local brands or imported foods), the app falls back to camera OCR. The user takes a picture of the ingredient list, and the Vision AI extracts and parses the text.
*   **Multilingual Synonym & Derivative Mapping**: The ingredient database maps synonyms in multiple languages (English, Spanish, French, German, Urdu/Hindi, etc.) to their master allergens (e.g., identifying *Maida* / *Suji* / *Gandum* or *Harina* as Wheat/Gluten; *Casein* / *Whey* / *Lactose* / *Khoya* as Milk).
*   **Custom Severity Toggles**: Set sensitivity levels per allergen:
    *   *Severe / Anaphylactic*: Zero-tolerance filter. Flags direct ingredients, hidden synonyms, chemical derivatives, and precautionary cross-contamination warnings (e.g., *"May contain traces of..."*).
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
*   **Barcode Lookup**: Instantly scan standard EAN/UPC barcodes. Connects to Open Food Facts and global product indices.
*   **Camera OCR (Gemini Integration)**: For unregistered products, the user captures a photo of the ingredient list. Gemini Vision OCR extracts the text, translates foreign terms, and checks them against the active allergen dictionary.

### B. Intelligence & Profile Customization
*   **AI Synonym & Derivative Mapping**: Automatically cross-references ingredients against an active allergen dictionary (e.g., identifying casein, whey, or lactoglobulin as Milk; albumin as Egg; arachis oil as Peanut; soy lecithin as Soy).
*   **Allergen Profile Toggles**: Customize profile for the top allergens: Peanuts, Tree Nuts, Milk, Eggs, Wheat/Gluten, Soy, Fish, Crustacean Shellfish, and Sesame. Users can add custom text filters (e.g., *“Sulfites”*, *“Tartrazine”*).
*   **Multilingual System UI**: Native interface support for major global languages (English, Spanish, French, German, Urdu).
*   **Offline Room DB Database**: Caches E-number classifications, allergen synonyms, and saved product safety logs for offline grocery shopping.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces safe allergen-free alternatives, E-number Halal/Allergen mapping, crowdsourced product registration, and emergency anaphylaxis rescue alerts.

### A. Global Safe Alternatives
*   **Allergen-Free Brand Suggestions**: When a scanned item is classified as Unsafe or Caution, the app automatically suggests 2-3 verified safe global alternatives (e.g., suggesting dairy-free milks or gluten-free flours).

### B. E-Number Halal & Allergen Mapping
*   **Additive Analyzer**: Analyzes E-numbers for both allergen derivatives (e.g., E322 soy lecithin) and Halal/Dietary status (e.g., animal-derived emulsifiers), integrating dietary checking into a single scan.

### C. Crowdsourced Product Registry
*   **Community-Driven Database**: Allows users to submit photos of new grocery items, ingredients, and barcodes to expand the shared global product directory.

### D. Emergency Anaphylaxis & First-Aid Guide
*   **Emergency Mode**: One-tap panic button that dials local emergency services (911, 999, 112, 1122) and alerts predefined emergency contacts with GPS location.
*   **Visual First-Aid Instructions**: Displays simple, animated, step-by-step instructions on how to handle an allergic reaction and administer an epinephrine auto-injector (EpiPen).

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing product barcodes and verified ingredient lists, synced to the client Room DB SQLite cache.
*   **Image Processing API**: FastAPI (Python) gateway that pre-processes captured label images (contrast adjustment, cropping) before passing them to the Gemini API for ingredient extraction.
*   **Privacy Engine**: All user allergen profiles and search histories are stored strictly on-device (Room DB). No personal medical data is uploaded to the cloud.