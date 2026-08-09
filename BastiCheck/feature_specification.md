# BastiCheck (بستی چیک) — Pakistan Neighborhood Reality Check Agent Spec

## Executive Overview & Vision
**BastiCheck (بستی چیک)** is an independent, hyper-local neighborhood intelligence and real-estate review platform designed specifically for the Pakistani urban housing market. 

Renting or buying a house or apartment in major Pakistani cities (Karachi, Lahore, Islamabad, Rawalpindi) is a major financial commitment. However, prospective tenants and home buyers are frequently misled by local real-estate agents (dealers) and property listings. Crucial local issues are systematically concealed:
*   **Water Scarcity & Tanker Dependency**: Many premier sectors (such as DHA Karachi, Clifton, or newly developed phases in Lahore) suffer from severe water shortages, forcing residents to spend thousands of rupees on private water tankers.
*   **Monsoon & Sewage Flooding**: During the summer monsoon rains, entire blocks and streets submerge in water due to clogged storm drains and back-flowing sewage.
*   **Street Crime & Security Risks**: Mobile snatching, car/motorcycle theft, and house robberies are highly localized, with specific streets or blocks acting as frequent crime hotspots.
*   **Winter Gas Outages**: Gas pressure drops to zero in many neighborhoods during winter (December to February), requiring expensive LPG cylinder replacements.
*   **Commercial Encroachment & Noise**: Residential blocks often face sudden commercialization, with schools, coaching academies, or marriage halls opening nearby, causing gridlocked traffic and noise.
*   **Erratic Fiber ISP Services**: High-speed internet availability (e.g., StormFiber, Nayatel, Transworld, PTCL Flash) varies block-by-block, making it difficult for remote workers to verify connectivity.

BastiCheck aggregates community forum chatter, municipal alerts, and verified resident reviews to give prospective buyers and renters an honest "Reality Check Scorecard" of any 4-block radius or apartment building before they sign a contract.

---

## 1. Targeted Local Context & Critical Metrics
The app evaluates urban blocks based on critical local infrastructure and safety parameters:
*   **Water Supply Reliability**: Days per week of municipal water supply vs. reliance on private tankers.
*   **Monsoon Flooding Risk**: Historical drainage performance during heavy rains.
*   **Security & Crime Index**: Real-time safety status of the block based on resident reports.
*   **Winter Gas Pressure**: Baseline gas supply stability during peak winter months.
*   **Verified Fiber ISPs**: Actual high-speed internet providers servicing the specific street.
*   **Zoning & Traffic Noise**: Level of traffic congestion, commercial encroachment, and proximity to loud commercial activities.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on creating a block-level search directory powered by daily web scrapers and a basic rating scorecard.

### A. Web Scraping & Aggregation Engine
A daily background worker crawls public resources for local neighborhood mentions:
*   **City Subreddit Scraper**: Extracts posts discussing specific sectors and blocks (e.g. DHA Phase 6, Johar Town G block, G-11 Islamabad) from r/karachi, r/lahore, and r/islamabad.
*   **Facebook Community Groups Monitor**: Scrapes public neighborhood welfare association groups, resident union portals, and buy/sell forums for local complaints regarding water, security, or sewage.
*   **Zameen.com Forum Scraper**: Harvests real-estate discussions and community question-boards discussing the livability of specific phases and projects.

### B. Core Mobile UX & Features
*   **Search by Locality & Block**: Users search by typing a specific neighborhood (e.g., *“Johar Town G3 Block, Lahore”* or *“DHA Phase 5 Block C, Karachi”*).
*   **Reality Check Scorecard**: Displays simple, easy-to-read rating bars: Water Supply, Flooding, Gas Pressure, Security, Fiber ISPs, and Noise.
*   **Pros & Cons Summary**: Quick green/red bullet-points summarizing community feedback (e.g., *“Pros: StormFiber & Transworld active. Cons: Zero gas pressure in winters; flooded 2 feet in 2024 monsoon”*).
*   **Bilingual Interface**: Native English and Urdu (اردو) toggle for all user reviews and interface text.
*   **Room DB Caching**: Allows users to save property profiles and browse them offline.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces crowdsourced verification, flood heatmaps, tanker bill calculators, and security database integrations.

### A. Verified Resident Submissions
*   **Verified Resident Badge**: Residents can submit anonymous, detailed reviews and get verified by uploading a photo of their utility bill (electricity, gas, or internet) matching the block's address (personal names and card details redacted).
*   **Live Infrastructure Pings**: Verified residents can ping current conditions (e.g., *"No gas today in Block D"* or *"Sewerage leakage on Street 4"*).

### B. Monsoon Flooding Heatmap
*   **Flooding Depth Map**: An interactive map overlay showing historical waterlogging levels on specific streets during monsoon seasons, helping buyers avoid low-lying, poorly drained streets.

### C. Water Tanker Cost Calculator
*   **Tanker Expense Estimator**: Estimates monthly water costs. Users input household size, and the app calculates expected tanker expenditures based on active prices in that locality (e.g., DHA Karachi tanker cartels).

### D. CPLC & Citizen Crime Registry
*   **Crime Radius Alerts**: Integrates public crime statistics (e.g., Karachi CPLC reports) and crowdsourced reports to display active street crime metrics (mobile snatching, vehicle theft) within a 500-meter radius of the searched property.

### E. Neighborhood Commercialization Tracker
*   **Zoning Permit Alerts**: Scrapes municipal development notices to warn users if a commercial school, coaching center, or marriage hall is planned on their residential street.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for geo-fencing the 4-block radius search zones and mapping coordinates.
*   **Data Protection**: Utility bills uploaded for resident verification are processed on the backend, verified, and instantly destroyed to protect user privacy.
*   **Optimized Edge Payloads**: Compresses map overlays and heatmaps to load quickly on low-bandwidth (2G/3G) connections during power outages.