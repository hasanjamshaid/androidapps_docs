# SolarCheck (سولر چیک) — Pakistan Solar Installation Auditor Spec

## Executive Overview & Vision
**SolarCheck (سولر چیک)** is an independent hardware authenticity verifier, solar system sizing planner, net-metering tracking utility, and installer review mobile application designed specifically for homeowners in Pakistan.

Faced with rapidly rising grid electricity tariffs, residential and commercial solar adoption in Pakistan is experiencing an unprecedented boom. However, the market is highly unregulated, leading to widespread consumer fraud:
*   **Counterfeit & Refurbished Panels**: Unscrupulous contractors frequently install low-quality B-grade or refurbished panels, relabeling them as genuine imported Tier-1 brands (e.g., Longi, Jinko, Canadian Solar, JA Solar).
*   **Cloned Inverters & Dangerous Cabling**: Bundling cloned or copycat hybrid inverters and installing under-rated DC wiring (e.g., using low-quality sub-6mm cables or non-copper wiring) poses severe fire hazards.
*   **Net-Metering Extortion**: Net-metering approvals (permitting selling excess power back to the grid) are intentionally delayed for months by local electricity distribution companies (DISCOs) unless unofficial premiums/bribes are paid.
*   **Vanishing Installers**: Homeowners are left without after-sales service or warranty support when fly-by-night installers shut down operations.

SolarCheck solves these challenges by providing panel serial validation, sizing/battery planners, crowdsourced net-metering wait trackers, and certified installer audit reviews.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific technical, regulatory, and grid challenges of the Pakistani solar market:
*   **Hardware Authenticity Database**: Cross-references scanned panel barcodes and serial numbers against the Alternative Energy Development Board (AEDB) registry of genuine imported Tier-1 shipments.
*   **Bilingual Sizing Planner**: Calculates optimal system size (3kW, 5kW, 10kW, 15kW+), inverter rating, and battery pairing options (Tubular lead-acid vs. Lithium-Iron Phosphate LiFePO4) based on the user's monthly DISCO bill units.
*   **DISCO Net-Metering Tracker**: Logs actual processing wait times and reported bribe/expediting costs for bi-directional green meters across different utility grids:
    *   LESCO (Lahore)
    *   K-Electric (Karachi)
    *   IESCO (Islamabad/Rawalpindi)
    *   MEPCO (Multan)
    *   FESCO (Faisalabad)
    *   GEPCO (Gujranwala)
*   **Earthing & Structural Auditing**: Guides checking wind-load structural engineering compliance (L-keys, rawalbolts structural verification) and proper copper earthing/grounding tests.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a panel serial scanner, billing-based sizing calculators, essential hardware checklists, and offline caching.

### A. Panel Verification & Sizing
*   **Panel Serial Scanner**: Point the mobile camera at the barcode/serial sticker on the solar panel to instantly check the model, wattage, import records, and AEDB registration status.
*   **Bilingual System Planner**: Users input their average monthly power consumption (in units/kWh). The app computes:
    *   Recommended solar array capacity (kW).
    *   Inverter specification recommendations (Hybrid, Off-Grid, or On-Grid).
    *   Battery backups capacity (Tubular vs Lithium requirements).
    *   Average price estimations (equipment cost vs. structural/installation cost).

### B. Safety Checklists & UI
*   **Essential Hardware Checklist**: Simple Urdu/English guides verifying key components: minimum 6mm copper DC wires, dedicated breakers, surge protection devices (SPDs), and direct earthing pits.
*   **Bilingual Nastaliq UI**: Full Urdu and English toggle using Nastaliq font styles.
*   **Offline Caching (Room DB)**: Caches the AEDB panel registry database and safety checklists locally, allowing users to verify panels on rooftops with poor mobile signals.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces crowdsourced net-metering registries, camera-based shading tools, invoice quote auditors, and installer ratings.

### A. DISCO Net-Metering Approval Tracker
*   **Net-Metering Wait Log**: A crowdsourced registry where users log their net-metering application dates, final activation dates, DISCO subdivision name, and any unofficial fees/bribes paid to get the meter installed. Displays live city-wide averages (e.g., *"LESCO average wait time in DHA Lahore: 75 days, reported premium: 35,000 PKR"*).

### B. Rooftop Shade & Generation Estimator
*   **Roof Shading Analyzer**: Uses the phone’s compass, gyroscope, and camera to overlay solar path angles. The user scans the sky from their rooftop, and the app calculates potential shading obstacles (trees, neighboring buildings) to estimate actual monthly power generation (kWh).

### C. Installation Quote Auditor
*   **Quote Bill Scanner**: Homeowners upload photos of their installer quotes. The AI OCR (Gemini) scans the bill, flags marked-up inverter prices, overpriced mounting structures, or under-rated cabling specs compared to verified market benchmarks.

### D. Verified Installer Rating Directory
*   **Rooftop Quality Ratings**: A directory of local solar installation companies rated by users on structural durability, earthing tests, net-metering assistance, and after-sales warranty support.