# KhaabaCheck (خابا چیک) — Restaurant Reality Agent Spec

## Executive Overview & Vision
**KhaabaCheck (خابا چیک)** is a hyper-local restaurant intelligence and bill transparency mobile application designed specifically for Pakistani diners.

Dining out ("Khaaba") is the primary recreational activity in urban Pakistan (Lahore, Karachi, Islamabad/Rawalpindi). However, consumers face a heavily manipulated marketing landscape:
*   **Paid Influencer Marketing**: Social media food bloggers (Instagram/TikTok) post glowing, paid reviews of mediocre restaurants, distorting real public consensus.
*   **Hygiene & Safety Failures**: Kitchen cleanliness is a major health concern, but properties conceal unhygienic conditions until raided by food authorities.
*   **Hidden Billing & Surcharges**: Eateries often add illegal service charges and apply incorrect provincial sales tax (GST/PST) rates.
*   **Terminal Evading Tactics**: Establishments frequently claim credit card machines are "offline" or "out of order" to force cash payments, avoiding digital tax trails and card processing fees.
*   **Exorbitant Weekend Wait Times**: Popular spots face massive queues on weekends, with wait times exceeding 90 minutes.

KhaabaCheck solves these issues by scraping local food forums, food authority logs, and user reviews to build a single, synthesized "Reality Check Profile" for every restaurant.

---

## 1. Targeted Local Context & Critical Metrics
The app evaluates and rates Pakistani restaurants on specific operational and compliance metrics:
*   **Hygiene & Stomach Warning Index**: Scans reviews for mentions of food poisoning, unhygienic practices, or stomach infections (e.g., keywords like *"pet kharab"*, *"food poisoning"*, *"dirty kitchen"*, *"stomach infection"*).
*   **Tax & Bill Transparency**: Identifies if the restaurant applies illegal service charges and validates if the correct GST/PST rate is being charged (e.g., 5% on card payments in Punjab vs. 15% on cash).
*   **Card Machine Reliability**: Tracks how consistently the restaurant accepts credit/debit card payments without claiming terminal failures.
*   **Signature Dishes & Hype vs. Reality Score**: Identifies what actual, non-sponsored users recommend as signature dishes, contrasting it against sponsored social media hype.
*   **Weekend Wait Times**: Estimated average wait times during peak hours (Fridays to Sundays, 8:00 PM to 11:00 PM).

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a search directory of restaurants with crowdsourced and scraped reviews, displaying scorecards for hygiene, pricing, and payment terminal reliability.

### A. Web Scraping & Aggregation Engine
A daily background worker crawls public resources for local dining reviews:
*   **Facebook Food Communities Monitor**: Scrapes organic mentions and complaints from major Pakistani culinary groups (e.g., "Halal Foodies", "Karachi Food Diary", "Foodies 'R Us", and local city-specific food circles).
*   **Google Maps & TripAdvisor Parser**: Scrapes maps reviews, using keyword-matching to detect complaints or praise regarding "hygiene", "poisoning", "pet kharab", "cards", "broken terminal", "tax", "service charge", and "wait time".
*   **Directory & Category Indexes**: Listings classified by City, Sector/Locality, Cuisine Type, and Price Slab (Budget, Mid-range, Fine Dining).

### B. Core Mobile UX & Features
*   **Reality Check Scorecard**: Visual sub-ratings: Hygiene safety, Bill transparency, Card machine availability, and Signature dishes.
*   **Pros & Cons Summary**: Quick green/red bullet-points compiled from reviews (e.g., *“Pros: Excellent mutton chops. Cons: Weak hygiene rating; frequently claims card terminal is offline”*).
*   **Bilingual Interface (Urdu & English)**: Complete native toggle between English and Urdu.
*   **Room DB Caching**: Caches searched restaurant profiles locally, allowing offline viewing. No login registration is required to search.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces food authority inspection records, bill tax calculators, card discount finders, and influencer hype filters.

### A. Food Authority Inspection Compliance Log
*   **Regulatory Alerts**: Scrapes news reports and official portals of provincial regulators (Punjab Food Authority - PFA, Sindh Food Authority - SFA, KP Food Authority - KPFA) to display a timeline of past inspections, fines, warnings, or sealing reports for the restaurant.

### B. Bill Tax & Bank Discount Auditor
*   **Receipt Scanner**: Users can photograph their dining bills. The app's OCR automatically calculates if the GST/PST charged matches provincial laws and flags illegal service charges.
*   **Card Discount Finder**: Scans and displays active credit/debit card bank discounts for the restaurant (e.g., *"HBL Cards get 30% off today (Friday)"*).

### C. AI Influencer Hype Filter
*   **Hype vs. Reality Score**: An AI engine that crawls social media posts (via hashtags/account names) of paid local food bloggers and compares their promotional ratings against organic user reviews on KhaabaCheck. It outputs a percentage score indicating how over-hyped the venue is.

### D. Crowdsourced Weekend Wait Times
*   **Live Queue Reports**: Allows diners currently at the venue to report wait times (e.g., *"30-minute queue at Kolachi DHA Phase 8"*), updating a live ticker on the restaurant's profile.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for locality searches and proximity mapping.
*   **Scraper Worker**: Python-based scraper utilizing proxy rotation to retrieve TripAdvisor and Google Maps reviews.
*   **Privacy Guard**: Uploaded receipt bill photos are processed securely on the backend, checked for tax rates, and permanently deleted from servers. No user personal information is stored.