# UrduColumn (اردو کالم) — Audio Urdu Columns & Reader Spec

## Executive Overview & Vision
**UrduColumn (اردو کالم)** is a consolidated, ad-free daily Urdu columnist directory, high-legibility Nastaliq reader, bilingual Text-to-Speech (TTS) audio player, and commute playlist mobile application designed specifically for readers and listeners in Pakistan.

Daily printed columns in major Urdu newspapers (e.g., Daily Jang, Daily Express, Daily Dunya, Daily Nawa-i-Waqt) written by well-reputed columnists (like Javed Chaudhry, Hassan Nisar, Orya Maqbool Jan, Yasir Pirzada, Hamid Mir, Rauf Klasra, Yasir Pirzada) are a major source of political critique, analysis, and historical knowledge in Pakistan. However, accessing and reading these columns is a highly fragmented experience:
*   **Ad-Cluttered & Non-Responsive Layouts**: Newspaper websites are loaded with heavy pop-ups, tracking scripts, and non-responsive scans of printed pages, making mobile reading frustrating.
*   **Visual Accessibility Barriers**: Older readers with failing eyesight struggle to read the tiny, low-contrast printed scripts on mobile screens.
*   **Commute Constraints**: Busy urban professionals want to consume columns during their daily traffic commutes but lack a safe, hands-free auditory option.
*   **Vocabulary Barriers**: Traditional columns frequently employ high-literacy Persian (Farsi) and Arabic vocabulary and idioms, making them difficult for younger, modern readers to comprehend fully.

UrduColumn solves these challenges by consolidating daily columns in a clean, ad-free Nastaliq reader with integrated Urdu Text-to-Speech (TTS) audio playback, playlist queues, and vocabulary explainers.

---

## 1. Targeted Local Context & Critical Metrics
The app is engineered to address the specific consumption patterns and linguistic complexities of the Pakistani media market:
*   **Columnist Follow Directory**: Follow top columnists across national Urdu dailies, compiling a personalized daily feed.
*   **Bilingual Urdu Text-to-Speech (TTS)**: Built-in audio playback synthesizing Urdu speech in a natural accent with speed adjustments (1.0x to 2.0x).
*   **Commute Audio Queue Playlist**: Allows users to add multiple columns to a daily listening queue for hands-free driving/multitasking.
*   **Bilingual Vocabulary Explainer**: Interactive popup clarifying complex Persian or Arabic vocabulary frequently used in formal Urdu columns.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a columnist follow registry, an ad-free Nastaliq reader, a bilingual interface, and offline caching.

### A. Core Directories & Reading Experience
*   **Columnist Directory**: Browse and follow writers by name and associated newspaper. A consolidated daily dashboard updates the moment columns are published.
*   **Ad-Free Nastaliq Reader**: A clean text viewer displaying columns in elegant Nastaliq Urdu script. Features custom font-size toggles, line-height adjustments, and a night/sepia mode for reduced eye strain.
*   **Bilingual Interface**: Native Urdu and English toggle using Nastaliq font styles.

### B. Mobile UI & Caching
*   **Offline Caching (Room DB)**: Automatically caches followed writers' daily columns locally, allowing offline reading when traveling or during power load-shedding.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces Urdu audio playback, commute queues, vocabulary explainers, and shareable status cards.

### A. Urdu Text-to-Speech (TTS) Player
*   **Hands-Free Voice Reader**: A native TTS audio button that reads the column aloud in a natural, clear Pakistani accent with speed control (1.0x, 1.25x, 1.5x, 2.0x). Perfect for users during daily road commutes or for elderly readers.

### B. Commute Queue Builder
*   **Daily Audio Playlists**: Allows users to add multiple columns to an audio queue (e.g. *"Play Hassan Nisar + Yasir Pirzada columns"*) for hands-free listening while driving.

### C. Urdu Vocabulary & Idiom Explainer
*   **Word Explainer**: Double-tapping a word pops up a simple Urdu and English dictionary definition mapping complex Persian/Arabic vocabulary to simple, common terms.

### D. WhatsApp Quote Status Card Exporter
*   **One-Tap Share Poster**: Highlight a quote from a column and export it as a beautifully styled card in Nastaliq Urdu for instant sharing to WhatsApp Status or Instagram Stories.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing processed de-biased news records, daily exchange rates, and historical logs, synced to the client Room DB SQLite cache.
*   **Scraper Worker**: Python-based scraper running hourly, parsing HTML/RSS feeds, checking duplicate articles via semantic embedding matching, and summarizing via Gemini API before admin validation.
*   **On-Device Privacy**: No tracking of user political preferences. Search history and read bookmarks are stored strictly on the client Room DB SQLite database.
