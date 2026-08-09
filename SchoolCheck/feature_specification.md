# SchoolCheck (اسکول چیک) — Parent Network & School Auditor Spec

## Executive Overview & Vision
**SchoolCheck (اسکول چیک)** is an independent, crowdsourced school and daycare intelligence platform designed specifically for parents in Pakistan. 

Private education in Pakistan is a multi-billion rupee industry. Parents pay premium tuition fees to top school chains (e.g., Beaconhouse, City School, Roots, Lahore Grammar School, LACAS, Froebel's) and premium daycares, expecting high-quality teaching and safe environments. However, official school websites and marketing brochures only display perfect board exam scores and pristine facilities. Crucial operational realities are systematically hidden:
*   **Hidden Fees & Surcharges**: Schools routinely charge unexpected fees (security fees, annual resources charges, sports fees, mandatory field trip charges) and force parents to purchase uniforms and textbooks from exclusive, overpriced vendors.
*   **High Teacher Turnover**: Top schools face massive teacher turnover. Classes are frequently left without permanent teachers or are assigned underqualified substitutes, forcing parents to pay for expensive private academies and tuitions.
*   **Inadequate Bullying & Safety Policies**: Many schools fail to address physical bullying, cyberbullying, or inappropriate teacher-student boundaries.
*   **CCTV & Transportation Security**: Lack of real-time daycare CCTV access and unregulated school van drivers raise significant child safety concerns.
*   **Pick-up & Drop-off Traffic Gridlock**: School zones cause daily gridlocks (e.g., Canal Road and DHA in Lahore, Clifton and KDA in Karachi), adding hours to daily commutes.

SchoolCheck aggregates community forum discussion, Google Maps reviews, and verified parent submissions to provide a "Reality Check Scorecard" for daycares and schools, giving parents the unvarnished truth before they pay heavy registration and security deposits.

---

## 1. Targeted Local Context & Critical Metrics
The app evaluates schools on parameters critical to Pakistani families:
*   **True Fee Transparency**: Complete mapping of hidden charges beyond the base monthly tuition.
*   **Teacher Stability Index**: How consistently teachers remain in their roles throughout an academic term.
*   **Bullying & Incident Handling**: Ratings on how proactively the school administration deals with student conflicts and behavioral issues.
*   **Security & Van Safety**: Quality of gate security, CCTV sharing policies, and van driver vetting.
*   **Transit Congestion impact**: Traffic delay estimates around the school during peak pick-up (12:30 PM to 2:30 PM) and drop-off (7:15 AM to 8:15 AM) hours.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a search directory of K-12 private schools and daycares, powered by daily community scrapers and a basic scorecard.

### A. Web Scraping & Aggregation Engine
A daily background worker crawls public resources for local school reviews:
*   **Facebook Parenting Groups Scraper**: Crawls discussions in major Pakistani parenting communities (e.g., "Soul Sisters Pakistan", "Karachi Parents Club", "Lahore Mothers Lounge", and local city-specific school groups) to parse organic feedback regarding specific schools.
*   **Google Maps Review Parser**: Scrapes maps reviews, using keyword-matching to detect complaints or praise regarding "fees", "canteen", "bullying", "teacher change", "admission test", "principal", "van", and "traffic".
*   **Curriculum-Based Directory**: Listings categorized by City, Locality, Fee Slab, and Curriculum (Cambridge O/A-Levels, Matric/FSc Board, International Baccalaureate - IB).

### B. Core Mobile UX & Features
*   **Reality Check Scorecard**: Visual sub-ratings: Hidden Costs, Teacher Stability, Bullying Management, Security & CCTV, and Pick-up Traffic.
*   **Pros & Cons Summary**: Quick green/red bullet-points compiled from reviews (e.g., *“Pros: Strong O-Level math department. Cons: Mandatory 15,000 PKR annual charges; school road blocked for 30 mins at home-time”*).
*   **Bilingual Interface (Urdu & English)**: Complete native toggle between English and Urdu.
*   **Offline Mode (Room DB)**: Caches searched schools and parent bookmarks to allow offline review reading. No login registration is required to search.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces crowdsourced verification, fee calculators, AI Roman-Urdu parsing, and a school van driver directory.

### A. Verified Parent Reviews
*   **Fee Voucher Verification**: Parents can post anonymous, detailed reviews and receive a "Verified Parent" badge by uploading a photo of their child's recent school fee voucher. The backend verifies the school name, date, and fee structure (redacting student names and CNICs).
*   **Anonymous Complaint Board**: A secure board where verified parents can highlight administration issues or safety incidents without fear of academic retaliation against their children.

### B. True Annual Fee Calculator
*   **Annual Attendance Cost Estimator**: Estimates the total cost of attendance. Users enter the baseline monthly tuition, and the app calculates:
    *   Annual registration and resource charges.
    *   Standard uniform and textbook costs.
    *   Expected exam registration charges (e.g., British Council O/A Level exam fees).
    *   Mandatory laboratory or sports equipment fees.

### C. AI Roman-Urdu Review Summarizer
*   **Bilingual Feedback Summarizer**: An NLP parser that translates and summarizes reviews written in English, Urdu, and Roman-Urdu (Urdu written in English script—standard in local chat groups) to write a concise warning summary (e.g., *"65% of reviews note that English and Science teachers were replaced mid-term."*).

### D. School Van & Route Registry
*   **Van Driver Directory**: A crowdsourced registry where parents share details, contact numbers, and routes of local school van services. Verified parents can rate van drivers on speed, safety, and punctuality.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for mapping school gate coordinates and calculating traffic delay zones.
*   **Data Protection**: Fee vouchers uploaded for parent verification are processed securely, validated, and permanently destroyed from servers to protect student privacy.
*   **Data Footprint**: Small database size (under 10MB) for Room DB local cache, optimized to load quickly on 3G/4G connections during power outages.