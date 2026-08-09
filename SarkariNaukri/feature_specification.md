# SarkariNaukri (سرکاری نوکری) — Pakistan Government Jobs Portal Spec

## Executive Overview & Vision
**SarkariNaukri (سرکاری نوکری)** is an automated daily government jobs aggregator, print classified ad OCR scraper, testing agency dashboard tracker, and bilingual application assistant mobile application designed specifically for job seekers in Pakistan.

In Pakistan, government employment (Basic Pay Scale grades BPS-1 to BPS-22 in ministries, police, military, healthcare, schools, and state-owned enterprises like WAPDA, PIA, and Pakistan Railways) is highly sought after for career stability. However, finding and applying for these positions is a highly fragmented, offline-heavy process:
*   **Scattered Newspaper Classifieds**: The majority of government job openings are published as low-resolution scanned image advertisements in print newspapers (Daily Jang, Express, Nawa-i-Waqt, Dawn). There is no central digital portal.
*   **Testing Agency Fragmentation**: Application processing and screening tests are split across multiple private testing services: National Testing Service (NTS), Open Testing Service (OTS), Punjab Testing Service (PTS), and Sindh Testing Service (STS), alongside provincial Public Service Commissions (FPSC, PPSC, SPSC, KPPSC, BPSC). Candidates must monitor dozens of separate sites to download roll number slips and check results.
*   **Manual Application Barriers**: Applying typically requires downloading and printing bank fee challans, physically depositing cash at National Bank of Pakistan (NBP) branches, and mailing a physical dossier of verified educational documents via post.

SarkariNaukri solves these pain points by offering a unified scanned job index, testing agency trackers, AI-powered ad eligibility readers, challan pre-fillers, and application trackers.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific administrative, grading, and testing structures of the Pakistani government recruitment system:
*   **Unified Jobs Index**: Aggregates job postings from national print newspapers and departmental websites, classifying them by Basic Pay Scale (BPS-1 to BPS-22), Department, and Province.
*   **Testing Services Hub**: A single tracking dashboard integrating FPSC, PPSC, SPSC, KPPSC, BPSC, NTS, OTS, and PTS schedules, roll number slips, and final merit list results.
*   **BPS Grade & Salary Reference**: Displays corresponding starting salaries, allowances, and pension structures associated with the BPS grade of the advertised job.
*   **Bilingual Interface**: Native Urdu and English toggle using Nastaliq font styles.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a centralized jobs directory, testing agency links, BPS/provincial filters, a bilingual interface, and offline caching.

### A. Core Directories & Tracking
*   **Centralized Jobs Index**: Daily scraped and manually verified directory of active government job listings, filtered by Department, City, Province, and BPS Grade.
*   **Testing Agency Portal**: Dashboard linking users directly to test date sheets, roll number downloads, and results pages across FPSC, PPSC, NTS, OTS, and PTS.
*   **Offline Cache (Room DB)**: Caches bookmarked job notices, exam syllabus guidelines, and department contact info locally.

### B. Mobile UI & Bilingual Support
*   **Nastaliq Urdu UI**: Complete Urdu interface toggle utilizing native Nastaliq font styles.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces AI advertisement parsers, challan helpers, profile-matched WhatsApp alerts, and mailing planners.

### A. AI Advertisement & Syllabus Parser
*   **Vision OCR Reader**: In-app OCR scanner (Gemini) that parses low-quality scanned print newspaper ads, automatically extracting key parameters: age limits (factoring in government age-relaxation policies), required qualifications (Matric, Inter, Bachelor's, Master's), quota availability (minority, women, disabled), and outlines the expected test syllabus.

### B. NBP Challan Form Helper
*   **Challan pre-filler**: Auto-fills and helps generate required NBP/SBP bank challan slips, providing checklists of nearby bank branches that accept deposits, as well as digital payment guides (e.g., e-Pay Punjab, e-Pay Sindh).

### C. Profile-Matched WhatsApp Alerts
*   **Profile Matching Bot**: Sends automated WhatsApp messages to job seekers the instant a new government job matching their specific age and educational qualifications is published.

### D. Mailing Dossier Checklist Planner
*   **Physical Mail Planner**: Step-by-step checklist of documents required for physical mailing (verified degrees, domicile certificates, CNIC copies, passport pictures, paid challan slips) to prevent application rejections.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing processed de-biased news records, daily exchange rates, and historical logs, synced to the client Room DB SQLite cache.
*   **NLP Pipeline**: Python-based scraper running hourly, parsing HTML/RSS feeds, checking duplicate articles via semantic embedding matching, and summarizing via Gemini API before admin validation.
*   **On-Device Privacy**: No tracking of user political preferences. Search history and read bookmarks are stored strictly on the client Room DB SQLite database.
