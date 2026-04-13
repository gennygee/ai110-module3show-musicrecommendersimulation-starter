import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Parses a dataset CSV into a list of dictionaries with correctly typed mathematical attributes."""
    songs = []
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(dict(row))
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Mathematically scores a song against User Profile targets, returning a total score and derivation list."""
    score = 0.0
    reasons = []

    # 1. Categorical: Genre Math (+2.0 Bonus)
    if 'genre' in user_prefs and song.get('genre') == user_prefs['genre']:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # 2. Categorical: Mood Match (+1.0 Bonus)
    if 'mood' in user_prefs and song.get('mood') == user_prefs['mood']:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # 3. Numerical: Proximity Scoring
    numerical_features = ['energy', 'valence', 'danceability', 'acousticness']
    for feature in numerical_features:
        if feature in user_prefs and feature in song:
            distance = abs(user_prefs[feature] - song[feature])
            points = 1.0 - distance
            score += points
            reasons.append(f"{feature.capitalize()} match (+{points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Iterates through the dataset evaluating each track to securely return the top k sorted recommendations."""
    scored_songs = []
    
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        # Join the list of reason strings into a single readable sentence
        explanation = ", ".join(reasons) if reasons else "No specific matches"
        scored_songs.append((song, score, explanation))
        
    # Rank the list by sorting descending based on the score (index 1 of the tuple)
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
