# BijliWatch (بجلی واچ) — Load Shedding & Outage Alerts Spec

## Executive Overview & Vision
**BijliWatch (بجلی واچ)** is a real-time load-shedding tracker and power outage notification mobile application designed specifically for Pakistani electricity consumers.

Load shedding is a daily reality in Pakistan. Electricity Distribution Companies (DISCOs like LESCO, IESCO, K-Electric, MEPCO, FESCO, GEPCO, PESCO, HESCO, SEPCO, QESCO) and the PITC CCMS publish schedules online, but checking them is highly inconvenient:
*   **14-Digit Reference Numbers**: Portals require a 14-digit reference number or feeder code, which users rarely know, particularly when away from home (e.g., at work, gym, or a restaurant).
*   **Unscheduled Outages**: Official schedules change without warning due to transformer trips, maintenance, grid failures, or dynamic demand management.
*   **Outdated Databases**: Existing government utilities apps suffer from frequent server downtime and outdated schedule feeds.

BijliWatch resolves this by translating the user's GPS coordinates into local Grid Station/Feeder codes using Uber H3 indexing, delivering pre-outage alerts, and mapping unscheduled blackouts in real time via crowdsourced reporting.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific patterns of the Pakistani electricity grid:
*   **Zero Reference Number Setup**: Automatically translates a GPS coordinate into the local grid feeder, removing the need for 14-digit numbers.
*   **Pre-Outage Reminders**: Alerts users 15–30 minutes before a power cut so they can turn on water pumps, charge laptops/phones, and ensure their UPS or solar batteries are prepared.
*   **Crowdsourced Unscheduled Blackouts**: Real-time crowd mapping of sudden local power failures (transformer bursts, line trippings) that happen outside official schedules.
*   **Urdu & English Alerts**: High-priority push notification banners written in both Urdu and English (e.g., *“Bijli Watch: DHA Phase 3 mein scheduled load-shedding 3:00 PM pe shuru hogi”*).

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers daily schedule scraping, GPS coordinate mapping, pre-outage alarms, and offline schedule viewing.

### A. DISCO Schedule Scraping Engine
*   **Portal Web Scraping**: A backend scraper that runs daily to extract weekly load-shedding schedules from official portals (LESCO, IESCO, K-Electric, and PITC CCMS) using active reference numbers and feeder IDs.
*   **Database Grid mapping**: Matches scraped schedules to specific feeder codes.

### B. Core Mobile UX & Features
*   **Pin-on-Map Registration**: Users register active locations (e.g., "Home", "Office") by dropping a pin on a map.
*   **Uber H3 Grid Querying**: The backend maps the coordinates to an Uber H3 Resolution 8 spatial cell (~737m). If that cell has a mapped Feeder Code, the app automatically subscribes the user to that feeder's schedule.
*   **Pre-Outage Push Notifications**: Sends an alert 15–30 minutes before scheduled power cuts (e.g., *"Power goes off at 3:00 PM in Gulberg Block B. Please charge your devices/UPS now"*).
*   **Bilingual System UI**: Complete Urdu and English interface support.
*   **Offline Room DB Storage**: Caches the weekly schedule locally, allowing users to check power schedules even during internet blackouts.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces crowdsourced blackouts, reference-to-GPS matching, battery advisors, and neighborhood energy heatmaps.

### A. Crowdsourced Unscheduled Blackout Tracker
*   **“Bijli Chali Gayi” (Power Out) Button**: A prominent widget on the app. If 3 or more users within the same H3 cell tap this button within 5 minutes, the app flags an active unscheduled outage for that cell.
*   **Outage Heatmaps**: Displays a live map of the city showing active blackouts in real time, alerting nearby residents before their own feeder potentially trips.

### B. Crowdsourced Feeder-to-GPS Mapping Registry
*   **Feeder Mapping Project**: Users can optionally link their 14-digit reference numbers to their GPS coordinates. The backend groups these inputs by matching Feeder IDs, incrementally building a high-resolution spatial map of Pakistan's feeder boundaries (data that is not publicly published by DISCOs).

### C. UPS & Solar Runtime Advisor
*   **Backup Charge Coordinator**: Suggests actions based on the scheduled outage duration (e.g., *"Expected load shedding today is 4 hours. Keep UPS load minimal to preserve battery"* or *"Load shedding starting in 20 mins; charge your UPS/solar batteries to maximum"*).

### D. Energy Reliability Heatmaps
*   **Neighborhood Energy Scores**: Displays average weekly load-shedding durations per sector (e.g., DHA DHA Phase 6 vs. Johar Town), helping prospective renters and buyers check neighborhood electricity stability.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension and Uber H3 Res 8 coordinates indexing.
*   **Schedule Parser**: Python-based scraper running scheduled cron-jobs to retrieve schedules. Uses proxy networks to prevent IP blockings from government DISCO portals.
*   **Data Security**: User location data and reference numbers are stored locally on the device (Room DB) by default. Cloud syncing is optional and encrypted.