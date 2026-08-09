# Taqreebaat (تقریبات) — Events Nearby App

## Executive Overview & Vision
**Taqreebaat (تقریبات)** is a hyper-local event discovery and real-time geo-proximity notification mobile platform designed specifically for the Pakistani market. 

Traditional event discovery in Pakistan is highly fragmented, scattered across WhatsApp groups, Facebook pages, closed university portals, and ticketing websites like Ticketwala and Bookme.pk. Taqreebaat solves this by aggregating these sources and connecting event organizers (tech conferences, Sufi & Qawwali nights, food galas, university expos, sports tournaments, and community gatherings) directly with nearby attendees based on live location coordinates.

Using a combination of automated daily scraping, on-demand scraping, and a lightweight mobile client, Taqreebaat provides sub-second geo-proximity matching to show users exactly what is happening around them.

---

## 1. Local Pakistan Context & Event Categories
Taqreebaat is customized for the cultural and social landscape of major Pakistani cities (Lahore, Karachi, Islamabad/Rawalpindi, Peshawar, Faisalabad, Multan, etc.). The app categorizes events to match local tastes:
*   **Sufi & Qawwali Nights**: Traditional musical gatherings, shrines (e.g., Data Darbar, Shah Jamal), and private performance venues.
*   **Food Galas & Festivals**: Local food street updates, restaurant launch events, family food galas (e.g., Lahore Eat, Karachi Eat).
*   **Campus & University Expos**: Student events, MUNs (Model United Nations), tech-fests, job fairs, and drama competitions (FAST, NUST, LUMS, IBA, GIKI, UET, Punjab University, etc.).
*   **Tech & Business Meetups**: Local developer meetups, startup pitch nights, and professional workshops (NICs, Plan9, local co-working spaces).
*   **Sports & Play**: Local cricket/futsal tournaments, screening spots for PSL/ICC matches, marathon runs, and hiking groups (e.g., Margalla hills treks).
*   **Arts, Culture & Theater**: Plays at Alhamra, Lok Virsa, PNCA, art exhibitions, and book launches.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP focuses on establishing a robust backend scraping engine and a clean, lightweight mobile interface for instant discovery.

### A. Automated Web Scraping Engine
A daily and on-demand scraping worker runs in the backend to pull events and populate the spatial database:
*   **Official Ticketing Platforms**: Automated scraping of major ticketing portals (Ticketwala, Bookme.pk, Sastaticket) for public ticketed events, including pricing, dates, and venues.
*   **Social Media & Cultural Portals**: 
    *   **Facebook Pages & Groups**: Scrapes public events from local community groups (e.g., "Lahore Events", "Karachi Startups") and cultural center pages (Alhamra, Lok Virsa).
    *   **Instagram Scraping**: Targeted extraction from verified event-organizing accounts and hashtags (e.g., `#qawwalinightlahore`, `#islamabadevents`).
*   **University Web Scraper**: Scrapes public student society pages and event registration portals of top universities.
*   **Location Geocoding API**: Uses open geocoders (or LLM parsing) to translate text-based venue descriptions (e.g., "Hall 2, Alhamra Art Council, Mall Road, Lahore") into exact latitude/longitude coordinates.

### B. Core Mobile UX & Features
*   **"Near Me" Map View**: A clean, interactive map showing pins of events active today or coming up this week.
*   **Geo-Proximity Feed**: A vertical list sorted strictly by distance from the user's current GPS location.
*   **Uber H3 Grid Querying**: Backend groups events using Uber H3 Resolution 8 spatial indexing (~737-meter hexagon resolution) for sub-second, database-friendly proximity queries.
*   **Direct Contact & Actions**:
    *   **Get Directions**: One-tap deep link to open Google Maps or Waze with pre-filled event coordinates.
    *   **Call/WhatsApp Organizer**: Direct call trigger or WhatsApp chat API link to contact organizers for reservations.
    *   **Official Booking Link**: Clean redirect button to the ticketing platform (e.g., Ticketwala checkout).
*   **Bilingual Localization**: Complete native interface toggle between English and Urdu (اردو) for wider accessibility.
*   **Data & Offline Optimization**:
    *   **Room DB Caching**: Caches events locally on the device to minimize data usage on mobile networks (3G/4G).
    *   **No Mandatory Login**: Users can browse and discover events immediately without signing up.

---

## 3. Phase 2: Advanced Growth Features
Once the MVP gains traction (determined by high daily active users and hit rates), the app will be upgraded with the following high-value features:

### A. Real-Time Proximity Alerts (Geofencing)
*   **Background Geofencing**: Low-battery-consumption background service that alerts the user when they enter an H3 cell containing an active event (e.g., "Hey! A Qawwali night is starting in 400m at Alhamra. Tap to view tickets.").
*   **Smart Filter Alerting**: Users can choose to subscribe only to specific alerts (e.g., notify me only of Food and Tech events within a 2km radius).

### B. Crowdsourced Event Submission (Promoter Hub)
*   **Verified Promoter Portal**: Small-scale organizers (underground bands, local board game clubs, small art studios) can directly upload their events.
*   **In-App Pin Setter**: Organizers drop a pin on the map to define the exact event coordinates.
*   **Moderation Dashboard**: Admin queue for verification to prevent spam, scams, or inappropriate content.

### C. Direct Ticketing & Checkout Integration
*   **Affiliate API Checkout**: Integration with ticketing providers to book, pay via local channels (EasyPaisa, JazzCash, Nayapay, Bank Transfer), and download PDF tickets directly within the app.
*   **In-App QR Tickets**: Store purchased event tickets within the app for quick scanning at the venue entrance.

### D. AI-Powered Personalization & Semantic Search
*   **Semantic Search Engine**: Users can search using natural language queries (e.g., "qawwali program under 1000 PKR this Sunday" or "startup events in DHA next week"). An LLM-based parser translates this into structured database query filters.
*   **Interest Profiling**: Learns from user clicks, bookmarks, and search history to automatically bubble up recommended events on their dashboard.

### E. Viral Social Sharing & Poster Generator
*   **Visual Share Cards**: Generates beautiful, customizable social media cards (for WhatsApp Status, Instagram Stories, or Facebook feed) featuring the event's Urdu/English title, date, venue, a mini-map snippet, and a referral QR code.
*   **Promo Code Referrals**: Users can share promotional discount codes for paid events directly with their social circles.

---


### Backend & Database Engine
*   **Spatial Database**: PostgreSQL equipped with PostGIS extension for accurate geographic point calculations.
*   **Spatial Indexing**: Uber H3 Resolution 8 spatial coordinates mapped to hexagons. This ensures that instead of performing expensive circular geo-distance queries on every request, the backend simply queries events belonging to the user's current H3 cell index and adjacent cells.
*   **API Framework**: FastAPI (Python) or Go-based backend for fast, concurrent location querying.