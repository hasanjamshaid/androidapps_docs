# GreenMeterCheck (گرین میٹر چیک) — Pakistan Net-Metering Auditor Spec

## Executive Overview & Vision
**GreenMeterCheck (گرین میٹر چیک)** is an independent net-metering bill auditor, solar inverter cloud API validator, bi-directional meter reader, and NEPRA regulatory dispute helper mobile application designed specifically for solar-powered households in Pakistan.

As utility grid tariffs escalate, solar net-metering (green meters) has become crucial for Pakistani middle-class households seeking to offset energy costs. However, verifying monthly utility billing is extremely difficult:
*   **Opaque Net-Billing Calculations**: Power distribution companies (DISCOs like LESCO, K-Electric, IESCO, MEPCO) issue highly complex bills. Imported units are split into peak and off-peak categories and charged at high, slab-based retail tariffs. Exported solar units are subtracted at a flat, much lower NEPRA buyback rate (currently around Rs. 22 per unit). The calculation is further complicated by Fuel Price Adjustments (FPA), Quarterly Tariffs Adjustments (QTA), and various government taxes.
*   **Under-Crediting of Solar Exports**: Solar users frequently notice that their physical inverters record higher export numbers than the solar units credited on their monthly DISCO bill, leading to uncompensated energy loss.
*   **Delayed Credit Roll-overs**: DISCOs routinely delay the payout or rolling over of excess net-metering credits, leaving users without their financial benefits for months.
*   **Frequent Policy Shifts**: Constant regulatory adjustments by NEPRA regarding solar taxes or buyback rates leave consumers confused.

GreenMeterCheck solves these issues by providing a net-billing simulator, inverter API auditor, real-time tariff alarms, and dispute letter builders.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific billing and grid structures of the Pakistani energy market:
*   **Multi-Grid Net-Billing Simulator**: Supports the custom billing formulas, taxes, and adjustments (FPA, QTA, Excise Duty, GST) for all major Pakistani DISCOs:
    *   LESCO (Lahore)
    *   K-Electric (Karachi)
    *   IESCO (Islamabad/Rawalpindi)
    *   MEPCO (Multan)
    *   FESCO (Faisalabad)
    *   GEPCO (Gujranwala)
*   **Inverter Cloud API Matcher**: Connects to the user's solar portal (Growatt, Solis, Huawei, GoodWe, Solis, Crown, Knox) to cross-reference actual solar exports against the units credited on the utility bill.
*   **Physical Meter LCD Reader**: Uses camera OCR to read the cycling numbers on the physical bi-directional green meter (differentiating between standard import/export display registers like 1.8.0 and 2.8.0).
*   **Bilingual Regulatory Alarms**: Real-time push alerts about NEPRA policy shifts, solar taxes, or national tariff updates in English and Urdu Nastaliq.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a net-billing simulator, NEPRA policy alarms, a bilingual interface, and offline caching.

### A. Core Simulator & Alerts
*   **Net-Metering Bill Simulator**: Input Peak/Off-Peak imported units and exported units from the physical bill or meter. The app calculates the exact expected bill amount, active slab rates, expected credit balance, and applicable duties/taxes under current NEPRA rules.
*   **NEPRA Policy Alarms**: Real-time push notifications explaining national solar tariff changes, buyback rate updates, and fuel adjustments in clear, conversational Urdu and English.

### B. Mobile UI & Caching
*   **Nastaliq Urdu UI**: High-legibility Urdu interface toggle using native Nastaliq font styles.
*   **Offline Tariff Database (Room DB)**: Caches active national tariff tables and NEPRA buyback regulations locally, ensuring the simulator works offline in basements or rural areas.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces inverter cloud integrations, meter screen scanners, DISCO scorecards, and dispute form pre-fillers.

### A. Inverter Cloud API Integration
*   **Discrepancy Auditor**: Securely links with the user's solar monitoring cloud account (Growatt ShineServer, Solis Cloud, Huawei FusionSolar, GoodWe SEMS). It extracts the exact monthly exported kWh and automatically flags billing errors if the DISCO bill under-credits solar exports by more than 5%.

### B. Bi-Directional Meter LCD Screen OCR Reader
*   **LCD Scanner**: A camera-based scanner optimized to read and parse the LCD screen of physical green meters. It guides the user to capture the cycling display values for code 1.8.0 (Active Import Peak/Off-Peak) and code 2.8.0 (Active Export Peak/Off-Peak) to maintain an independent, daily usage log.

### C. DISCO Credit Accuracy Scorecard
*   **Compliance Tracker**: A crowdsourced database comparing credit roll-over delays, billing error rates, and average customer service response times across different regions.

### D. NEPRA & DISCO Dispute Form Generator
*   **Form Pre-Filler**: Pre-fills official billing complaint forms with the user's customer number, details of under-reported export units, and calculated credit discrepancies. It generates a print-ready PDF for submission to the DISCO's Customer Services Director or the NEPRA Ombudsman.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing active utility tariff tables, tax brackets, and crowdsourced DISCO compliance ratings, synced to the client Room DB SQLite cache.
*   **Inverter Fetcher Worker**: Python-based worker service communicating with Growatt, Solis, and Huawei APIs to fetch daily generation and export logs securely.
*   **Privacy Guard**: Solar inverter credentials and monitoring tokens are encrypted and stored strictly on-device to ensure user security.