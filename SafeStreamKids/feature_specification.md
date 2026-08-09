# SafeStream Kids (سیف اسٹریم کڈز) — Android App Spec

## Executive Overview & Vision
**SafeStream Kids (سیف اسٹریم کڈز)** is a parent-controlled YouTube wrapper application designed specifically for Pakistani families. It enforces a strict **Strict Whitelist Model** to protect children from the algorithmic rabbit holes of mainstream video platforms.

In Pakistan, children are increasingly exposed to digital screens, but standard YouTube and YouTube Kids present major risks:
*   **Inappropriate Local Advertising**: Unfiltered local ads on YouTube Pakistan often promote online betting, dating services, or adult products.
*   **Mixed Cultural & Language Exposure**: Auto-play algorithms routinely funnel children from high-quality educational videos to low-quality cartoon channels featuring inappropriate Urdu/Hindi slang or violent themes.
*   **Mobile Data Package Drain**: High-resolution video streaming quickly depletes expensive mobile 4G/LTE data packages, leading to unexpected billing shocks for parents.

SafeStream Kids solves this by stripping out all ads and restricting video playback exclusively to parents' approved whitelists or curated collections vetted by a trusted local community of Pakistani parents.

---

## 1. Targeted Local Context & Features
The app is tailored to the connectivity and cultural needs of Pakistani households:
*   **Ad-Stripping Sandbox Player**: An embedded custom player that blocks all YouTube ads, ensuring children never see inappropriate betting, gambling, or adult-themed commercial banners.
*   **Data Package Guard**: A parental toggle that limits video resolution strictly to 240p or 360p when on mobile data, saving expensive mobile internet packages.
*   **Urdu & Local Language Curation**: Focuses on curating moral stories, nursery rhymes, and educational content in local languages (Urdu, Punjabi, Sindhi, Pashto, Balochi) and bilingual (Urdu-English) STEM programs.

---

## 2. Phase 1: MVP (Minimum Viable Product) Specification
The MVP delivers a secure, offline-caching, ad-free sandboxed video player with a PIN-protected parent whitelist setup.

### A. Parent Whitelist Portal
*   **Access Control**: The Parent Portal is locked behind a 4-digit PIN, pattern, or device biometric check (Fingerprint/Face Unlock).
*   **Direct Share-to-App Approvals**: Parents can approve content by pasting a YouTube link or sharing a video/playlist/channel directly from the native YouTube app to SafeStream Kids.
*   **Pre-Vetted Local Starter Packs**: A default starter library curated by early-childhood educators in Pakistan, containing:
    *   Urdu Nursery Rhymes (Nazmein)
    *   Moral Stories (Urdu Kahaniyan)
    *   Basic Science & Math in Urdu/English
    *   Islamic/Moral teachings for children

### B. Strict Sandboxed Child UI
*   **Icon-Driven Interface**: A highly visual, kid-friendly dashboard using simple category icons (e.g., Stories, Learn, Music).
*   **Zero External Search**: Kids can only search or browse within the parent-approved whitelisted database.
*   **No Mandatory Account Creation**: Children can start watching immediately without setting up accounts or providing personal details.
*   **Bilingual System UI**: Easy system-wide toggle between English and Urdu.

---

## 3. Phase 2: Advanced Growth Features
For the scale-up phase, the app integrates crowdsourced curation, screen-time schedules, AI text parsing, and offline video downloading.

### A. Community-Curated Parent Registry
*   **Global Parent Whitelists**: Allows Pakistani parents to share their curated playlists (e.g., "Best Grade 3 STEM Videos in Pakistan").
*   **Safety Score & Flag Tags**: A peer-review system where parents rate and tag community-submitted videos for language, pacing, and cultural appropriateness (e.g., tags like "Mixed Language Slang", "Loud Jump Scares").
*   **Trust Scoring**: Parents who contribute reliable, highly-rated whitelists gain higher contributor levels.

### B. AI-Powered Transcript & Description Scanning
*   **Urdu/Hindi Slang Filter**: An AI backend script that processes video transcriptions and descriptions to automatically scan for, flag, and filter out inappropriate local language, slang, or aggressive behavior.

### C. Advanced Screen Time & Bedtime Schedules
*   **Schedules & Blackout Hours**: Parents can define allowed active hours (e.g., 4:00 PM to 6:00 PM only) and set automatic lock times (e.g., no viewing after 8:30 PM).
*   **Friendly Lock Screen**: Once the timer runs out, the screen locks with a friendly, localized screen in Urdu/English (e.g., *"Time to do homework! / Time to sleep!"*).

### D. Multi-Profile Management
*   **Individual Child Profiles**: Up to 5 child profiles per family with age-appropriate whitelist levels (Toddler 2–4, Kids 5–8, Pre-Teen 9–12) and customized library assignments.

### E. Wi-Fi Downloader & Offline Cache
*   **Home Wi-Fi Cache**: Allows parents to select whitelisted videos to download locally to the device's storage while on home Wi-Fi, permitting ad-free, offline playback during road trips or power outages.

---

## 4. Backend & Database Specification
*   **Local Storage**: Android Room Database (SQLite) on the client device storing the whitelisted video metadata, categories, and child profile settings.
*   **Scraper & API Backend**: FastAPI (Python) backend to validate submitted YouTube URLs, fetch channel/playlist metadata via YouTube API, and cache community safety score ratings.
*   **Privacy Engine**: Strict compliance with COPPA-equivalent guidelines. Child profiles are completely local; no viewing history, search queries, or device IDs are sent to the cloud. Only the parent account details are stored securely.
