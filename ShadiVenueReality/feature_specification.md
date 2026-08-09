# ShadiVenue (شادی وینیو) Reality Check Agent — Spec

## Executive Overview & Vision
**ShadiVenue (شادی وینیو) Reality Check Agent** is an independent, hyper-local event venue review aggregator and intelligence platform designed specifically for the Pakistani wedding and corporate event market. 

In Pakistan, wedding events (Shadi, Mehndi, Baraat, Walima) are major financial milestones, often costing millions of rupees. However, choosing a venue (marriage hall, marquee, hotel ballroom, or farmhouse) is a process riddled with hidden costs and operational issues. Venue owners frequently hide critical flaws:
*   **Cooling Failures**: Air conditioning systems that struggle to cool large marquees in summer heat (40°C+).
*   **Generator Surcharges**: Outrageous hourly billing for diesel generators during load shedding.
*   **Monopoly Policies**: Heavy fines if hosts bring external stage decorators, DJs, or caterers.
*   **Government Curfews**: Sudden enforcement of the 10:00 PM / 11:00 PM curfew or the Punjab "One-Dish" regulatory rules, leading to abrupt event shutdowns or police raids.

ShadiVenue solves this by running background scrapers that pull unfiltered feedback from Google Maps, Facebook groups, wedding forums, and local vendor reviews. It presents hosts and event planners with an honest "Reality Check Scorecard" for each venue before they book.

---

## 1. Targeted Local Context & Critical Metrics
The app evaluates Pakistani venues on specific operational metrics that define the event experience:
*   **AC & Climate Control Reliability**: How well does the cooling perform during peak summer (May to September) or the heating during peak winter (December to January)?
*   **Generator Backup Policy**: Is generator power included in the rent, or is there a hidden hourly diesel charge? How quickly does the backup power kick in during load shedding?
*   **Vendor Policy & Monopolies**: Does the venue enforce a list of overpriced in-house decorators and caterers? What is the penalty fee for bringing outside vendors?
*   **Curfew & Compliance Record**: Has the venue been sealed or fined by the local government (e.g., Lahore Cantonment Board, Capital Development Authority, Karachi Metropolitan Corporation) for violating sound limits, curfews, or one-dish laws?
*   **Parking & Security Capacity**: Does the venue have dedicated parking? Are guests harassed by external parking cartels or forced valet fees?

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on establishing a database of major venues across cities like Lahore, Karachi, and Islamabad/Rawalpindi, backed by automated scraping engines.

### A. Web Scraping & Aggregation Engine
A backend scraping worker runs daily to harvest venue-specific details:
*   **Google Maps Reviews Parser**: Extracts and parses reviews of venues. It uses keyword-matching to detect issues like "cooling", "generator", "light chali gayi", "curfew", "police", "parking", and "hidden charge".
*   **Facebook Group Monitor**: Scrapes mentions and discussions of wedding halls/marquees from public and large local groups (e.g., "Soul Sisters Pakistan", "Pakistani Brides", local city community groups).
*   **Core Venue Directory**: Venue listings classified by City, Locality (e.g., DHA, Gulberg, Clifton, Bahria Town, Saddar), Guest Capacity (e.g., 200, 500, 1000+), and Venue Type (Marquee, Marriage Hall, Farmhouse, Hotel).

### B. Core Mobile UX & Features
*   **Reality Check Scorecard**: Instead of a generic 5-star rating, venues display a sub-rating breakdown (AC Cooling, Generator policy, Parking capacity, Vendor rules).
*   **Pros & Cons Bullet Feed**: A quick summary of common complaints and praise from past guests and vendors (e.g., *“Cons: AC went off twice; 5,000 PKR per hour generator fee charged afterwards”*).
*   **Urdu & English Bilingual Interface**: The entire directory can be searched and read in Urdu (اردو) or English.
*   **Direct Dial & Maps**: Quick button to call the venue sales office directly or open the exact gate coordinates in Google Maps.
*   **Offline Cache (Room DB)**: Caches searched venues and bookmarks to save mobile data usage. No user registration is required to view reviews.

---

## 3. Phase 2: Advanced Growth Features
Once the MVP has captured initial traction, the application will be upgraded with verified crowdsourcing, cost estimators, and AI-powered text analysis.

### A. Verified Host & Vendor Reviews
*   **Verified Host Submission**: To prevent fake positive reviews by venue owners, hosts can submit an anonymous review and get a "Verified Host" badge by uploading a photo of their booking invoice (with personal details redacted).
*   **Event Vendor Portal**: Photographers, catering managers, DJs, and makeup artists can post ratings about the venue's backstage rooms, power sockets, load-in access, and management behavior.

### B. AI-Powered Review Summarization
*   **Review Summarizer**: A local LLM or API-driven text summarizer that condenses hundreds of reviews into a single paragraph (e.g., *"Overall, 85% of reviews note excellent catering quality, but 40% warn that the cooling was insufficient for summer afternoon events."*).

### C. "Hidden Cost" Calculator
*   **Extra Cost Estimator**: An interactive calculator that estimates the actual total price of a venue. Users input the base venue rent and estimated guest count, and the app calculates:
    *   Estimated generator fuel costs (based on average load-shedding duration for that locality).
    *   Stage decorator penalty fees.
    *   Catering taxation additions (local provincial sales tax).
    *   Valet tipping and security guard costs.

### D. Live Compliance Tracker
*   **Regulatory Alerts**: Displays a history of government inspections and penalties for the venue, warning users if a hall has been repeatedly fined for violating local rules (such as Lahore's one-dish law or Islamabad's strict 10:00 PM music curfew).

### E. Side-by-Side Venue Compare
*   **Comparison Engine**: Allows users to compare up to three venues side-by-side on all major parameters (price, capacity, AC rating, decorator policy).

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for exact location-based mapping of wedding venues.
*   **Storage**: Client-side Room DB caching for offline browsing of bookmarked venues.
*   **Privacy Guard**: Booking invoices uploaded for verified host reviews are processed on the backend, verified manually or via automated OCR, and permanently deleted from the server to protect user privacy. No user PII is ever displayed.