# GuenhwyvarLabs

This repository contains various experimental projects. The `entertainment_recommender` directory holds a simple Flask web application that asks a few questions and recommends an album, movie, or TV show based on your mood and genre preferences.
Recommendations are fetched from the public iTunes Search API so an internet connection is required.

## Entertainment Recommender App

### Setup

1. Install dependencies (preferably in a virtual environment):

```bash
pip install -r entertainment_recommender/requirements.txt
```

2. Run the app locally:

```bash
python entertainment_recommender/app.py
```

The application will start on [http://localhost:5000](http://localhost:5000). Open this URL in your browser to answer the questions and receive a recommendation.

The app will attempt to fetch a random result from the iTunes Search API based on your chosen mood, medium, and genre. If the request fails, it falls back to a small built-in list of suggestions.

