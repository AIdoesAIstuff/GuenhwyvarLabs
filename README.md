# Music Recommendation Web App

This project is a simple full‑stack music recommendation app. The React frontend asks a short questionnaire and the Node.js backend fetches an album suggestion from the Last.fm API.

## Local macOS Setup
1. Install Node.js using [Homebrew](https://brew.sh/):
   ```bash
   brew install node
   ```
2. Install dependencies and start the app:
   ```bash
   npm install
   npm start
   ```
   The application builds the React app and serves everything from Express at <http://localhost:3000>.

Set the Last.fm API key in the environment before starting:
```bash
export LASTFM_API_KEY=your_lastfm_key
```

## Docker
Build and run the container:
```bash
docker build -t music-rec-app .
docker run -p 3000:3000 -e LASTFM_API_KEY=your_lastfm_key music-rec-app
```
Then open <http://localhost:3000> in your browser.

Environment variables are used for API credentials. Replace `your_lastfm_key` with your own key.
