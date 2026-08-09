# Siyahat (سیاحت) — Resort & Rental Reality Agent Spec

## Executive Overview & Vision
**Siyahat (سیاحت) — Resort & Rental Reality Agent** is a specialized travel review aggregator and intelligence platform designed specifically for the Pakistani domestic tourism market. 

Pakistan's domestic tourism has boomed in areas like the Northern Valleys (Murree, Nathiagali, Swat, Kalam, Naran, Hunza, Skardu, Fairy Meadows) and coastal beaches (Karachi, Kund Malir, Gwadar). However, travelers face frequent disappointments due to misleading, highly-photoshopped hotel and cabin listings on booking sites. Properties routinely hide severe operational flaws:
*   **Heating & Hot Water Failures**: Geysers and room heaters that do not work in freezing temperatures.
*   **Power Load Shedding**: Lack of generator/UPS backups during mountain valley blackouts.
*   **Road Landslides & Accessibility**: Sudden road closures due to landslides or heavy snowfall, or tracks that are completely inaccessible by normal passenger cars.
*   **Local Transport Cartels**: High transport cartel fees, where local jeep unions block private vehicles and charge tourists exorbitant rates (e.g., for treks to Lake Saif-ul-Mulook or Fairy Meadows).
*   **Erratic Internet & Mobile Signals**: Unreliable Wi-Fi and mobile networks (SCOM, Zong, Telenor), a major issue for remote workers and content creators.

Siyahat acts as an independent watchdog agent, running daily and on-demand scraping pipelines across local travel forums and review sites to expose the unpolished reality of hotels, resorts, and vacation rentals.

---

## 1. Targeted Local Context & Critical Metrics
The app rates Pakistani accommodations based on specific structural and environmental challenges:
*   **Heating & Geyser Efficiency**: Is hot water available 24/7, or is it restricted to limited hours in the morning? Do room heaters work during power outages?
*   **Backup Power Reliability**: Does the venue run a generator, solar system, or UPS during load shedding? Are guests charged extra hourly fuel fees for generator usage?
*   **Road difficulty & Jeep Cartel Status**: Can the resort be reached in a standard sedan? Does it require a 4x4 vehicle? Are guests forced to pay local jeep cartel unions?
*   **Mobile Signal & Wi-Fi Quality**: Real network signal strength for SCOM (the primary carrier in Gilgit-Baltistan), Zong, Telenor, and Jazz, along with verified download speeds.
*   **Hygiene & Bathroom Reality**: True cleanliness status of bedsheets, blankets, and bathrooms, ignoring promotional catalog photos.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on aggregating reviews for popular Northern Pakistani destinations using automated scraping of travel communities and mapping them to a custom reality scorecard.

### A. Multi-Source Scraping Pipeline
A daily and on-demand background worker aggregates listings and reviews:
*   **Facebook Travel Communities Parser**: Scrapes discussion threads and review posts from major Pakistani travel groups (e.g., "Karakoram Club", "Travel Beautiful Pakistan (TBP)", "Travelers of Pakistan").
*   **Booking.com & Google Maps Scraper**: Pulls reviews for hotels in targeted valleys, using text filters to extract complains about "geyser", "heater", "light", "landslide", "road", "cartel", "jeep", and "dirty".
*   **Road & Weather Alerts Aggregator**: Automatically fetches road blockages, landslide warnings, and weather alerts from the NDMA (National Disaster Management Authority), PMD (Pakistan Meteorological Department), and local tourist police social media accounts.

### B. Core Mobile UX & Features
*   **Reality Check Scorecard**: Replaces basic stars with sub-ratings: Heating/Geyser, Power Backup, Mobile Signals (SCOM/Zong/Telenor), Road Access, and Hygiene.
*   **Transport Cartel Surcharge Warning**: Alerts users if a hotel is located on a track where local transport unions force guests to pay high jeep rates.
*   **Bilingual Localization**: Seamless interface toggle between English and Urdu (اردو).
*   **Offline Cache (Room DB)**: Caches searched hotels, road alerts, and bookmarked listings so travelers can access them in valleys with zero internet connection.
*   **No Login Barrier**: Allows users to check reviews and road conditions instantly without register screens.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces crowdsourced verification, live mobile signal reporting, and AI-driven roman-Urdu analysis.

### A. Live Crowd Room & Bathroom Audits
*   **Geotagged Photo Uploads**: Allows checked-in travelers to post real, unfiltered room and bathroom photos. The app uses EXIF metadata verification to ensure the photo was captured at the resort's coordinate boundaries.
*   **Verified Host Status**: Reviews from hosts who upload their booking receipts (with personal PII redacted) are highlighted with a verification badge.

### B. Verified Network Speed Reports
*   **In-App Speed & Signal Logger**: Integrates a lightweight speed test tool. Checked-in guests can run a test that logs their download speed, ping, and mobile carrier (SCOM/Zong/Telenor) directly to the hotel’s profile.

### C. AI Roman-Urdu Review Summarizer
*   **Bilingual NLP Parser**: Translates and analyzes reviews written in English, Urdu, and Roman-Urdu (Urdu written in English script—very common in Pakistani forums) to compile a concise list of warnings (e.g., *"Overall, 80% of reviews praise the views, but 45% warn that the geyser is shut off after 10 AM."*).

### D. Crowdsourced Jeep Cartel Price Index
*   **Jeep Fare Registry**: A directory where travelers report what they paid for local jeep hires (e.g., Naran to Lake Saif-ul-Mulook, Raikot Bridge to Fairy Meadows jeep point) to establish a baseline fair price index and prevent overcharging.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for geo-proximity queries and mapping resort coordinates.
*   **Scraping Worker**: Python-based scraper utilizing rotated proxy arrays to avoid IP bans from Booking.com and Google.
*   **Data Optimization**: Minimizes data payload size for slow mountain edge connections (2G/3G) by compressing images and caching static content.