# SaleScout (سیل اسکاؤٹ) — Pakistan Sale Discovery Engine Spec

## Executive Overview & Vision
**SaleScout (سیل اسکاؤٹ)** is a location-based mobile application, crowdsourced deal directory, automated price tracker, and notification engine designed specifically for shoppers in Pakistan.

Consumers in Pakistan love discounts, but discovering genuine sales is a noisy, fragmented process:
*   **The SMS Spam Overload**: Fashion retailers, restaurants, and grocery chains constantly bombard consumers with promotional SMS text blasts (using brand masks like "SAPPHIRE", "KHAADI", "IDEAS", "ALFATAH"). Consumers are overwhelmed by spam, yet they frequently miss clearance sales from the brands they actually care about.
*   **Invisible In-Store Clearance**: Major physical clearances inside shopping malls (such as Emporium Mall, Packages Mall, Lucky One Mall, Centaurus, Giga Mall) are often unadvertised online. Shoppers only discover them by physically walking past the storefront.
*   **Fake Discount Inflation**: A common retail trick involves inflating original prices right before a holiday event (e.g., Eid, Independence Day, Blessed Friday) to make a standard price look like a "Flat 50% Off" deal.

SaleScout solves these challenges by providing a clean, centralized discovery engine where users follow specific brands, browse deals by local shopping mall, monitor seasonal sale calendars, and stack credit card offers.

---

## 1. Targeted Local Context & Critical Metrics
The app is tailored to the specific characteristics of the Pakistani retail and e-commerce environment:
*   **Bilingual Brand Follow System**: Follow local retail, dining, and online brands, including:
    *   *Apparel & Fashion*: Sapphire, Khaadi, Ideas by Gul Ahmed, J. (Junaid Jamshed), Outfitters, Maria B., Limelight.
    *   *E-commerce & Retail*: Daraz (11.11, 12.12), Elo (Export Leftovers), Bagallery, Al-Fatah, Metro Cash & Carry.
    *   *Dining*: KFC, McDonald's, OPTP, local restaurant chains.
*   **Mall-Centric Location Filters**: Pinpoints active in-store promotions inside major shopping malls or within a 5km radius of the user's coordinates.
*   **Payday & Eid Sale Calendar**: Tracks local purchasing seasons, including monthly paydays (1st to 5th of the month), Eid-ul-Fitr, Eid-ul-Adha, August 14th Independence Day, and Blessed/White Friday.
*   **Bank Card Discount Stacking**: Calculates the net savings by layering active bank credit card partnerships on top of standard store sales (e.g., indicating that an Outfitters 30% sale can be combined with an additional 15% Bank Alfalah card discount).

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a brand follow registry, mall-centric location alerts, a payday/holiday calendar, and offline caching.

### A. Brand & Location Directory
*   **Brand Follow System**: A checkbox selection menu where users follow their preferred brands. The app sends push notifications *only* when followed brands launch verified sales.
*   **Mall & Proximity Filters**: Browse deals by City, Major Shopping Mall, or a 5km GPS radius.
*   **Bilingual Sale Calendar**: Displays timelines of upcoming clearances, payday promotions, and holiday events.

### B. Mobile UI & Caching
*   **Bilingual Nastaliq UI**: Complete Urdu and English interface toggle utilizing native Nastaliq font styles.
*   **Offline Cache (Room DB)**: Caches followed brand details, active deals, and mall directories locally, ensuring the app functions inside basement shopping centers with poor cellular coverage.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces AI discount calculators, crowdsourced deal uploaders, WhatsApp alert bots, and card discount stacking.

### A. AI True-Discount Value Ranker
*   **Price Inflation Tracker**: Analyzes historical item price logs to verify if a brand's advertised discount (e.g. "Flat 50%") is a genuine price cut or if original prices were marked up beforehand, ranking deals by true savings value.

### B. Crowdsourced In-Store Flash Deal Uploader
*   **In-Mall Deal Sharing**: Allows shoppers inside malls to snap photos of unadvertised clearance racks, discount banners, or store tags. Uploads are geofenced and instantly shared with other users tracking that mall.

### C. WhatsApp Digest Alert Bot
*   **WhatsApp Webhook**: Integrates with a verified WhatsApp Business line. Users receive a weekly automated message summarizing active sales from their followed brands and nearby malls.

### D. Bank Card Offer Stacking Engine
*   **Stacked Deal Calculator**: Integrates with active bank card promotion directories to calculate the absolute lowest net price (combining the store's sale rate with the user's credit card partner deal).

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for geo-fencing mall boundaries and calculating the 5km deal radius, synced to the client Room DB SQLite cache.
*   **Scraper Worker**: Python-based scraper that crawls brand websites, Instagram handles, and SMS discount registries to update promotion databases.
*   **Anonymity Guard**: All user-submitted crowdsourced photos strip metadata (GPS coordinates, camera EXIF data) to protect user privacy.