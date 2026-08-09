# KhoonCheck (خون چیک) — Pakistan Blood & Donor Registry Spec

## Executive Overview & Vision
**KhoonCheck (خون چیک)** is an independent, verified volunteer donor directory, welfare blood bank locator, and emergency communication mobile application designed specifically for patients and families in Pakistan.

In Pakistan, securing blood for emergency transfusions (due to surgeries, road accidents, childbirth, or regular thalassemia and leukemia requirements) creates high-stress situations. Desperate families are often exploited by illegal, professional/commercial donors (*pesha-war* donors). These commercial donors are frequently drug addicts carrying transmissible diseases (Hepatitis B/C, HIV, Syphilis, Malaria) and routinely present forged screening certificates. Meanwhile, public and welfare blood bank inventories are highly fragmented, with no centralized registry.

KhoonCheck acts as an audited, independent volunteer network, connecting patients directly with verified donors, trusted welfare blood banks, and crowdsourced warning registries to prevent patient exploitation.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific supply chain and safety challenges of the Pakistani healthcare landscape:
*   **Verified Volunteer Registry**: Voluntarily registered donors are verified via SMS OTP checks and mandatory last-donation-date logs to enforce the healthy 90-day donation cooldown period.
*   **Welfare & Public Blood Bank Directory**: Maps contact details, locations, and estimated stock availability for trusted national welfare blood centers, including:
    *   Fatimid Foundation (Lahore, Karachi, Peshawar, Multan, etc.)
    *   Indus Hospital & Health Network (IHHN) Blood Centers
    *   Sundas Foundation (specialized for thalassemia and leukemia patients)
    *   Pakistan Red Crescent Society (PRCS / Hilal-e-Ahmar)
*   **Commercial Donor ("Pesha-war") Blacklist**: A crowdsourced, verified blacklist of phone numbers, CNICs, and names associated with professional donors who demand money or fake screening documents.
*   **Bilingual Emergency Banner Generator**: Automatically compiles patient requirements into structured, high-contrast digital cards (Urdu Nastaliq and English) optimized for viral sharing on WhatsApp Status, Instagram Stories, and Facebook Groups.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers an OTP-verified volunteer registry, a welfare blood bank directory, a structured emergency request generator, and offline caching.

### A. Core Registries & Search
*   **Verified Volunteer Database**: Search for local volunteer donors by City, Locality (e.g., DHA, Gulberg, Clifton, Saddar), Blood Group (including rare negative types), and active cooldown status.
*   **Welfare Blood Bank Index**: A detailed directory of trusted welfare blood banks with direct dial buttons, Google Maps location links, and standard pricing/exchange guidelines (e.g., if a replacement donor is required).

### B. Emergency request & Mobile UI
*   **Structured Request Card Generator**: Form collects: Patient Name, Blood Group, Units needed, Hospital Name/Room, Contact number, and Date/Time. Generates a clean digital banner in English and Urdu Nastaliq to avoid messy, unformatted social media posts.
*   **Bilingual Interface**: Native Urdu and English toggle.
*   **Offline Cache (Room DB)**: Stores saved blood bank contact lines, emergency guides, and recent requests locally for access inside hospital wards.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces commercial donor warning registries, specialized thalassemia/dengue matching portals, location-aware WhatsApp alert bots, and transfusion checklists.

### A. Commercial Donor & Scam Blacklist
*   **Scam Number Database**: Allows families to flag phone numbers of individuals who demand cash, sell blood bags, or present fake laboratory screening papers. Flagged numbers are blocked across the platform after administrator verification.

### B. Thalassemia & Dengue SDP Matching Portal
*   **Recurring Thalassemia Donor Match**: Connects families of thalassemia children with a pool of dedicated recurring monthly donors.
*   **Dengue Platelets (SDP) Registry**: A specialized registry for matching Single Donor Platelets (SDP / Megathrombocytes) during seasonal Dengue outbreaks in major cities.

### C. Location-Aware Automated WhatsApp Alert Bot
*   **WhatsApp API Integration**: Integrates with a verified WhatsApp Business webhook. When a verified emergency request is submitted, the system automatically sends local alerts to registered donors matching the blood type within a 5km radius (using H3 Resolution 8 spatial cells).

### D. Transfusion Screening Checklist
*   **Screening Safety Guide**: A simple, interactive guide explaining to families what screening tests (Hepatitis B, Hepatitis C, HIV, Syphilis, Malaria) the blood bag *must* undergo at the lab before transfusion, empowering them to verify safety logs at the hospital.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for geo-fencing lookup of nearby volunteers, synced to the client Room DB SQLite cache.
*   **OTP Gateway**: Integration with local Pakistani SMS gateways (e.g., Jazz, Telenor, Zong APIs) for secure donor verification.
*   **Privacy Engine**: Volunteer donor phone numbers are masked by default. Call connections are routed through a secure, anonymous bridge to prevent spam and protect female donor privacy.