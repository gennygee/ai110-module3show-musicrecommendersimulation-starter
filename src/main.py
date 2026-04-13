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

        print("\n[ Top Recommendations ]\n" + "="*50)
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"#{i} | {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f} Pts")
            print(f"   Why: {explanation}")
            print("-" * 50)


if __name__ == "__main__":
    main()
