# SuyiGasWatch (سوئی گیس واچ) — Gas & CNG Tracker Spec

## Executive Overview & Vision
**SuyiGasWatch (سوئی گیس واچ)** is a real-time gas pressure monitor, CNG station tracker, and LPG price utility mobile application designed specifically for Pakistani consumers.

Pakistan faces a chronic natural gas shortage. The two major state utilities—SNGPL (Sui Northern Gas Pipelines Limited, serving Punjab, KP, and Islamabad) and SSGC (Sui Southern Gas Company, serving Sindh and Balochistan)—enforce scheduled gas load shedding and face low pressure, especially during winter cooking hours (December to February). Additionally:
*   **CNG Station Shutdowns**: Compressed Natural Gas (CNG) stations (essential for budget commuters and public transport) face scheduled weekly shutdowns under government gas-saving rotations.
*   **LPG Retail Price Gouging**: When pipeline gas disappears, families rely on LPG cylinders. However, local shopkeepers routinely sell cylinders far above the Maximum Retail Price (MRP) regulated by OGRA (Oil and Gas Regulatory Authority).

SuyiGasWatch solves these challenges by combining official schedules, real-time crowdsourced gas pressure pings, CNG station queues, and official LPG price limits in a unified, bilingual dashboard.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific patterns of the Pakistani gas distribution network:
*   **Gas Pressure Levels**: Tracks the actual usability of gas (High, Low/Medium—sufficient for tea but not cooking, Zero—stove not lighting) rather than just scheduled times.
*   **Weekly CNG Rotations**: Maps active/inactive CNG stations based on provincial scheduled closures (Punjab vs. Sindh/Balochistan).
*   **Official OGRA LPG Limits**: Displays the government-controlled price per kilogram and per standard 11.8kg domestic cylinder to prevent retail overcharging.
*   **Bilingual Alerts**: Push notification alerts in both Urdu and English (e.g., *“Gas pressure dropping in Clifton Block 5. Please turn on electric stoves”*).

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers official gas timetables, weekly CNG schedules, OGRA LPG price alerts, and offline schedule viewing.

### A. Official Schedule Scrapers
*   **SNGPL & SSGC Scraper**: A backend worker that scrapes daily press releases and load-shedding tables from SNGPL and SSGC official sites.
*   **CNG Rotation Scraper**: Pulls scheduled weekly CNG closure notices from government energy portals.
*   **OGRA Price Monitor**: Scrapes the monthly domestic LPG cylinder price notification from the official OGRA website.

### B. Core Mobile UX & Features
*   **Slab-Based Location Search**: Users select their city and sector (e.g., *“Sector G-9, Islamabad”* or *“Gulshan-e-Iqbal Block 13, Karachi”*).
*   **Uber H3 Grid Querying**: The backend maps the coordinates to an Uber H3 Resolution 8 spatial cell (~737m) to match pipeline sectors.
*   **LPG Price Dashboard**: Displays the current month's official OGRA price per kg and per standard 11.8kg domestic cylinder.
*   **Bilingual System UI**: Complete Urdu and English interface support.
*   **Offline Schedule Cache**: Caches gas and CNG schedules in a local Room DB, allowing users to view timetables during power and internet blackouts.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app integrates crowdsourced pressure pings, CNG station queues, a verified LPG distributor directory, and electric stove calculators.

### A. Crowdsourced Real-Time Pressure Pings
*   **"Check Pressure" Button**: A simple widget where residents ping their current gas pressure (High, Low, Zero). 
*   **Pressure Heatmaps**: If multiple users in the same H3 cell report Zero or Low pressure, the system flags the sector and sends push alerts (e.g. *"Gas pressure dropping in Sector G-9. Switch to electric geysers/LPG stoves now"*).

### B. CNG Station Queue Tracker
*   **CNG Queue Reports**: Allows public transit drivers and car owners to report active queues and wait times (e.g., *"30-minute queue at PSO Kalma Chowk"* or *"CNG station open, zero queue"*).

### C. Verified LPG Distributor Directory
*   **LPG Supplier Registry**: A directory of local LPG suppliers with contact numbers and parent ratings. Enables reporting of distributors who sell above OGRA-approved prices, mapping bad actors.

### D. Electric Stove vs. Gas vs. LPG Cost Estimator
*   **Fuel Cost Advisor**: Input household cooking hours to calculate the estimated monthly cost of running pipeline gas vs. LPG cylinders vs. electric induction stoves (based on active electricity slab rates), helping families choose the most economical option.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension and Uber H3 Res 8 coordinates indexing.
*   **Scraper Engine**: Python-based scraper running scheduled crawls on SNGPL, SSGC, and OGRA portals.
*   **Offline Optimization**: Minimizes data payload size for slow mobile connections (2G/3G) by caching static content and using lightweight JSON payloads.