# MazdoorCheck (مزدور چیک) — Pakistan Skilled Labor Registry Spec

## Executive Overview & Vision
**MazdoorCheck (مزدور چیک)** is a free, commission-free, voice-assisted daily wage labor directory, rate index, and safety compliance mobile application designed specifically for skilled and semi-skilled workers (*Mazdoor*) and homeowners in Pakistan.

The daily wage labor market in Pakistan is highly informal. Every morning, plumbers, electricians, painters, carpenters, and masons gather at neighborhood street intersections (*Chowks*) in major urban centers, waiting for homeowners or contractors to hire them. This model presents severe challenges:
*   **Job Discovery Inefficiency**: Workers often wait for hours and return home without finding work, resulting in lost income.
*   **Wage Exploitation**: Homeowners frequently underpay workers due to lack of standard rates, while middleman contractors (*Thekedars*) take heavy commission cuts.
*   **Aesthetic & Safety Risks**: Workers operate without basic safety protocols (leading to frequent falls or electrocution), while homeowners struggle to verify the trust and skill level of workers.
*   **Literacy Barriers**: Most daily wage workers are illiterate or semi-literate, making standard text-based gig apps unusable.

MazdoorCheck solves these pain points by offering a free, direct-dial, bilingual, and voice-assisted digital directory that connects consumers directly with workers gathered at their local Chowks.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific socio-economic and literacy characteristics of the Pakistani labor market:
*   **Chowk-Level Directories**: Organizes worker listings based on the physical *Chowks* where they gather daily in each city (e.g., DHA Chowk, Karsaz Chowk, Chungi No. 9, G-9 Markaz Chowk).
*   **Commission-Free Direct Dialing**: Connects homeowners directly to workers via mobile phone calls. The app charges no fees, allowing workers to retain 100% of their daily wage.
*   **Standard Wage Index**: Displays typical daily and hourly market rates per skill category (specialists, skilled, and helpers) to prevent consumer overcharging and worker exploitation.
*   **Bilingual & Voice-First Accessibility**: Clean Urdu Nastaliq interface supported by audio playback of category names and buttons to assist semi-literate workers.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a Chowk-mapped direct-dial directory, standard daily wage guides, an Urdu-first interface, and offline caching.

### A. Chowk-Mapped Labor Directory
*   **Local Intersections Directory**: Search and filter workers by City, Local Chowk, and Skill (Electrician, Plumber, Painter, Carpenter, Mason/Helper).
*   **Direct Phone Connection**: One-tap calling to connect directly with the worker's mobile number.

### B. Wage Guides & Accessibility
*   **Standard daily Wage Index**: A reference table displaying average daily/hourly market rates for standard labor tiers (Specialist, Skilled, Helper) and specific jobs (e.g., ceiling fan installation, water geyser repair, wall painting per sq ft).
*   **Bilingual Nastaliq UI**: Native interface toggle between English and Urdu (using clean Nastaliq font rendering).
*   **Offline Cache (Room DB)**: Caches local worker lists and wage index tables, allowing users to search listings in low-connectivity areas.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces voice-recorded reviews, illustrated audio safety guides, contractor verification badges, and proximity-based matching.

### A. Voice-Recorded Reviews & Audio Profiles
*   **Voice-Memo Ratings**: Homeowners can record a quick audio review about a worker's performance. The backend translates the audio into Urdu text for consumers and generates an audio playback file for the worker, allowing them to hear their own reviews and build a digital reputation profile.
*   **Audio Profile Summaries**: Allows workers to listen to their overall profile ratings, job counts, and saved feedbacks in audio format.

### B. Illustrated & Audio-Guided Safety Checklists
*   **Urdu Safety Manuals**: Interactive, illustrated step-by-step safety guides in Urdu (e.g., verifying electrical shutoffs, securing scaffolding harnesses, proper ventilation during chemical painting) with optional voice-over reading to prevent work site accidents.

### C. Contractor-Vouched Skill Badges
*   **Peer Verification**: A validation system where local builders or contractors (*Thekedars*) can vouch for a worker's competence and reliability, granting them a "Vouched" trust badge.

### D. GPS Proximity Matching
*   **Nearby Labor Locator**: Connects homeowners with active, available workers located within a 2km radius for urgent household repairs.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL with PostGIS extension for geo-fencing the 2km search radius, synced to the client Room DB SQLite cache.
*   **Speech-to-Text API**: Integration with bilingual (English/Urdu) speech-to-text engines to transcribe voice reviews left by homeowners.
*   **Privacy Guard**: Homeowners can choose to hide their phone numbers when calling workers, routing calls through an anonymous proxy number.