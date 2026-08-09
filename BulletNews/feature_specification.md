# UrduKhabrein (اردو خبریں) — No-Nonsense Bullet News Spec

## Executive Overview & Vision
**UrduKhabrein (اردو خبریں)** is a swipeable, no-scroll 60-word news summary card directory, AI-powered de-biased aggregator, and bilingual audio news reader mobile application designed specifically for consumers in Pakistan.

Public news consumption in Pakistan is heavily impacted by information overload and polarization:
*   **Sensationalism & Clickbait**: News outlets and their social media channels are flooded with clickbait headlines, polarizing talk-show debates, and infinite feeds designed to maximize scrolling time.
*   **Time-Wasting Media**: Users waste hours navigating social media apps just to find basic, high-impact updates (e.g., school holiday extensions, petrol rate changes, currency rates).
*   **Lack of Clean Urdu bullet News**: While English de-biased news aggregators exist, the Pakistani general public lacks a fast, clean, and objective news companion presented in high-quality Urdu Nastaliq.

UrduKhabrein solves these issues by presenting the day's top factual updates in clean, swipeable 60-word bullet cards, completely removing comment sections, political arguments, and clickbait.

---

## 1. Targeted Local Context & Critical Metrics
The app is tailored to the specific consumption patterns and language requirements of the Pakistani public:
*   **Swipeable 60-Word Bullet Cards**: News is formatted as single, swipeable cards. Each card contains a headline and 3-4 bullet points (max 60 words) in clear, legible Nastaliq Urdu script.
*   **Daily Economic Metrics Widget**: Displays crucial daily Pakistani indicators at a glance:
    *   Petrol and Diesel prices per liter (including announcements of upcoming price changes).
    *   USD / EUR / SAR / AED to PKR currency exchange rates.
    *   Gold price per Tola (24-Karat).
    *   Local weather forecasts.
*   **De-Biased Fact Index**: Aggregates stories from multiple news publishers (e.g., Jang, Dawn, BBC Urdu, Express, ARY News, Dawn News), using AI to strip emotional bias and compile purely factual points.
*   **Urdu Text-to-Speech (TTS) Voice News**: Native audio engine reading the Urdu summary aloud, providing a hands-free news listening experience.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers swipeable Nastaliq cards, an AI-powered scraping pipeline, daily price widgets, and offline caching.

### A. Core Swipe Cards & Aggregator
*   **Swipeable No-Scroll Cards**: Users swipe left/right to browse the day's top news cards. No scrolling feeds, no advertisements, and no comment sections to prevent time-wasting.
*   **AI Scraper & Summarizer**: Backend scraper crawls major Pakistani news portals, groups duplicate articles, filters out sensationalist opinion pieces, and uses Gemini to generate the de-biased 60-word Urdu bullet card.
*   **Daily Metrics Sidebar**: A quick dashboard displaying petrol, currency exchange, and gold rates.

### B. Mobile UI & Caching
*   **Bilingual Nastaliq UI**: Complete Urdu and English toggle using native Nastaliq font styles.
*   **Offline Cache (Room DB)**: Automatically stores the top 30 news cards of the day locally, ensuring users can read news offline during daily commutes or power load-shedding.

---

## 3. Phase 2: Advanced Growth Features
In Phase 2, the app introduces Urdu audio playback, de-biased source compare indexes, high-impact alerts, and shareable status cards.

### A. Urdu Text-to-Speech (TTS) Audio Playback
*   **Hands-Free Voice News**: A native TTS audio button that reads the 60-word Urdu card aloud in a natural, clear Pakistani accent. Perfect for users during daily road commutes or for elderly and visually-impaired readers.

### B. De-Biased Source Compare Index
*   **Transparency Check**: Expanding a card displays original source links side-by-side (e.g. Dawn, Jang, BBC Urdu) to verify report neutrality and check sources.

### C. Restricted Emergency Push Alerts
*   **Zero-Spam High-Impact Alerts**: Push notifications are disabled by default and restricted strictly to massive public safety announcements (e.g., smog-related school closures, nationwide power grid failures, or extreme weather warnings).

### D. Shareable WhatsApp Status Card Generator
*   **One-Tap Share Poster**: Automatically generates a high-contrast graphic poster card of the news bullet in Urdu Nastaliq, optimized for instant sharing on WhatsApp Status or Instagram Stories.

---

## 4. Backend & Database Specification
*   **Database**: PostgreSQL storing processed de-biased news records, daily exchange rates, and historical logs, synced to the client Room DB SQLite cache.
*   **NLP Pipeline**: Python-based scraper running hourly, parsing HTML/RSS feeds, checking duplicate articles via semantic embedding matching, and summarizing via Gemini API before admin validation.
*   **On-Device Privacy**: No tracking of user political preferences. Search history and read bookmarks are stored strictly on the client Room DB SQLite database.
