# Day 2: Building a Local Voice Agent with FastAPI + TTS

Today I built a local text-to-speech web app using FastAPI. The app takes user input, converts it to speech, and serves the generated MP3 back in the browser for instant playback.

## Highlights
- Built a simple HTML/JS front-end for input and playback
- Created a FastAPI route to generate TTS audio
- Organized an `audio_files/` directory to store generated files with unique UUIDs
- Configured static serving of MP3s for instant user access
- Attempted to integrate Murf AI TTS API, but switched to focus on local demo due to API 404 errors

## Tech Stack
- Python (FastAPI)
- HTML / JavaScript
- Murf AI API (integration planned)
- UUID / file management

## Running locally
1. `pip install -r requirements.txt`
2. `uvicorn app:app --reload`
3. Open `http://127.0.0.1:8000` in your browser

## Next
- Fix Murf AI TTS API calls
- Polish the UI
- Add authentication

> *Pushing my limits, one day at a time!* 🚀
