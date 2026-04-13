"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}") 

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        "Adversarial / Conflicted": {"genre": "classical", "mood": "sad", "energy": 0.99, "danceability": 0.9}
    }

    for name, prefs in profiles.items():
        print(f"\n\n>>> EVALUATING PROFILE: {name} <<<")
        print(f"Targets: {prefs}")
        
        recommendations = recommend_songs(prefs, songs, k=5)

        print("\n" + "="*125)
        print(f"| {'Rk':<2} | {'Title':<26} | {'Artist':<20} | {'Scor':<4} | {'Why/Derivation'}")
        print("-" * 125)
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            title = song['title'][:25]
            artist = song['artist'][:19]
            print(f"| #{i:<1} | {title:<26} | {artist:<20} | {score:<4.2f} | {explanation}")
        print("=" * 125)


if __name__ == "__main__":
    main()
