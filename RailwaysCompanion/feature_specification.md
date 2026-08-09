# SastaSafar (سستا سفر) — Pakistan Railways Passenger Companion Spec

## Executive Overview & Vision
**SastaSafar (سستا سفر)** is an independent, crowdsourced live train delay tracker, coach quality auditor, offline schedule index, and ticket quota alert mobile application designed specifically for Pakistan Railways passengers.

Rail travel is a major mode of long-distance transport in Pakistan, used by millions of passengers daily. However, the travel experience is plagued by systematic inefficiencies:
*   **Massive Schedule Delays**: Trains are frequently delayed by hours due to aging track infrastructure, weather (e.g., winter fog in Punjab), or operational issues, leaving passengers stranded at platforms.
*   **Variable Coach Quality**: Standards of cleanliness, air conditioning cooling, power outlet functionality, and running water vary drastically across different coaches, even within the same class (Economy, AC Standard, AC Business, AC Sleeper).
*   **Buggy Official Systems**: The official Pakistan Railways mobile application and live tracker are slow, inaccurate, and frequently crash during peak holiday reservation windows (Eid, summer vacations).
*   **Platform Price Gouging**: Food vendors at intermediate stations regularly overcharge passengers for water, tea, and meals, ignoring official retail price sheets.

SastaSafar solves these pain points by offering an offline-cached schedule and fare index, a passenger-powered live tracking grid, detailed coach audits, automated reservation alerts, and platform price verifiers.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific routing, ticketing, and service conditions of the Pakistan Railways network:
*   **Bilingual Fare & Class Index**: Supports fare calculations across all travel classes, including AC Sleeper, AC Business, AC Standard, AC Parlour, and Economy.
*   **Crowdsourced Delay Tracking Grid**: Passengers currently on board use GPS tracking (validated against active rail corridor boundaries) to check in and report delays at stations, building a real-time tracking map for waiting travelers.
*   **Coach Quality Scorecards**: Crowdsources ratings of specific coach numbers (e.g., *“AC Business Coach #4 on Karakoram Express”*) based on cooling, charging plugs, clean bedding, and toilet hygiene.
*   **Station Platform Price Auditor**: Directories detailing food quality at platforms, pricing comparison (to prevent stall vendors from overcharging passengers), and station cooling/waiting room status.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a bilingual train schedule directory, crowdsourced live delay tracking, an offline network map, and offline caching.

### A. Core Schedules & Delay Tracking
*   **Bilingual Train Directory**: Search train routes by city (e.g., Lahore to Karachi, Rawalpindi to Multan). Displays official departure/arrival timings and fare tiers.
*   **Live Delay Tracker**: Passengers on board a train toggle a "Share Live Location" switch (verifying coordinates match the active railway track). The app broadcasts their delay duration to waiting users at upcoming stations.
*   **Offline Route Database**: Local database storing all PR train routes, timings, and station stops, allowing passengers on rural tracks with no mobile signals to view schedules.

### B. Mobile UI & Caching
*   **Bilingual Nastaliq UI**: Complete Urdu and English toggle using Nastaliq font styles.
*   **Offline Cache (Room DB)**: Caches the PR timetable database and route maps locally, ensuring the schedule checker works offline in remote regions.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces coach quality audits, seat alert systems, platform food price checks, and refund calculators.

### A. Coach-Level Quality Auditor
*   **Rooftop Quality Ratings**: A directory where passengers log their coach number and rate critical service parameters: AC cooling efficiency, working charging plugs, fan operations, bathroom cleanliness, and running water. Helps travelers select the best coach number during booking.

### B. Automated Seat Quota Alert Engine
*   **Reservation Monitor**: Scrapes the official PR web booking portal. Sends real-time push or WhatsApp alerts when seat quotas release or waitlist reservations clear.

### C. Station Platform Price Auditor
*   **Platform Price Auditor**: Directories detailing platform food stalls and pricing comparisons, warning travelers of rate-gouging stall vendors charging above official rates at intermediate stops.

### D. Delay Refund Claim Advisor
*   **Refund Form Pre-Filler**: Pre-fills refund forms explaining Pakistan Railways rules regarding compensation for delays exceeding 3-5 hours.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing PR timetable schemas, local branch coordinates, and active ticket allocations, synced to the client Room DB SQLite cache.
*   **Scraper Worker**: Python-based scraper that crawls official government gazettes to update schedule charts.