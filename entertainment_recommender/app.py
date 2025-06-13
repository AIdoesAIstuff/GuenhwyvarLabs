from flask import Flask, render_template, request
import random
import requests
from typing import Optional

app = Flask(__name__)

RECOMMENDATIONS = {
    "Album": {
        "happy": {
            "pop": "Future Nostalgia - Dua Lipa",
            "rock": "American Idiot - Green Day",
            "hip hop": "The College Dropout - Kanye West",
            "electronic": "Discovery - Daft Punk",
        },
        "sad": {
            "pop": "21 - Adele",
            "rock": "OK Computer - Radiohead",
            "hip hop": "To Pimp a Butterfly - Kendrick Lamar",
            "electronic": "Immunity - Jon Hopkins",
        },
        "energetic": {
            "pop": "1989 - Taylor Swift",
            "rock": "Nevermind - Nirvana",
            "hip hop": "DAMN. - Kendrick Lamar",
            "electronic": "Cross - Justice",
        },
        "relaxed": {
            "pop": "Lemonade - Beyoncé",
            "rock": "Parachutes - Coldplay",
            "hip hop": "Illmatic - Nas",
            "electronic": "Play - Moby",
        },
    },
    "Movie": {
        "happy": {
            "action": "Guardians of the Galaxy",
            "comedy": "The Grand Budapest Hotel",
            "drama": "The Pursuit of Happyness",
            "sci-fi": "Back to the Future",
        },
        "sad": {
            "action": "Logan",
            "comedy": "Lost in Translation",
            "drama": "Manchester by the Sea",
            "sci-fi": "Children of Men",
        },
        "energetic": {
            "action": "Mad Max: Fury Road",
            "comedy": "Scott Pilgrim vs. the World",
            "drama": "Whiplash",
            "sci-fi": "Edge of Tomorrow",
        },
        "relaxed": {
            "action": "Wonder Woman",
            "comedy": "Chef",
            "drama": "Big Fish",
            "sci-fi": "Her",
        },
    },
    "TV Show": {
        "happy": {
            "action": "The Mandalorian",
            "comedy": "Brooklyn Nine-Nine",
            "drama": "Ted Lasso",
            "sci-fi": "Doctor Who",
        },
        "sad": {
            "action": "The Punisher",
            "comedy": "BoJack Horseman",
            "drama": "The Handmaid's Tale",
            "sci-fi": "Black Mirror",
        },
        "energetic": {
            "action": "Stranger Things",
            "comedy": "Parks and Recreation",
            "drama": "24",
            "sci-fi": "The Expanse",
        },
        "relaxed": {
            "action": "MacGyver",
            "comedy": "The Office",
            "drama": "Friday Night Lights",
            "sci-fi": "Star Trek: The Next Generation",
        },
    },
}

MOODS = ["happy", "sad", "energetic", "relaxed"]
GENRES = [
    "pop",
    "rock",
    "hip hop",
    "electronic",
    "action",
    "comedy",
    "drama",
    "sci-fi",
]
MEDIUMS = ["Album", "Movie", "TV Show"]


def fetch_from_itunes(mood: str, medium: str, genre: str) -> Optional[str]:
    """Fetch a random suggestion from the iTunes Search API."""
    search_term = f"{mood} {genre}".strip()
    media_map = {
        "Album": "music",
        "Movie": "movie",
        "TV Show": "tvShow",
    }
    media = media_map.get(medium)
    if not media:
        return None

    params = {"term": search_term, "media": media, "limit": 50}
    try:
        resp = requests.get("https://itunes.apple.com/search", params=params, timeout=5)
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if results:
            choice = random.choice(results)
            return choice.get("trackName") or choice.get("collectionName")
    except Exception as exc:
        print(f"API fetch failed: {exc}")
    return None


def get_recommendation(mood: str, medium: str, genre: str) -> str:
    """Return a recommendation, trying the online API first."""
    suggestion = fetch_from_itunes(mood, medium, genre)
    if suggestion:
        return suggestion

    mood = mood.lower()
    genre = genre.lower()
    mood_data = RECOMMENDATIONS.get(medium, {}).get(mood)
    if not mood_data:
        return "No recommendation available."
    return mood_data.get(genre, "No recommendation available.")


@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None
    if request.method == "POST":
        mood = request.form.get("mood", "").lower()
        medium = request.form.get("medium", "")
        genre = request.form.get("genre", "").lower()
        recommendation = get_recommendation(mood, medium, genre)
    else:
        mood = medium = genre = ""
    return render_template(
        "index.html",
        moods=MOODS,
        mediums=MEDIUMS,
        genres=GENRES,
        recommendation=recommendation,
    )


if __name__ == "__main__":
    # When running inside Docker we need to listen on all interfaces so the
    # mapped port is reachable from the host.
    app.run(debug=True, host="0.0.0.0", port=5000)
