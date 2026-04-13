# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
**VibeFinder 1.0 (CLI-Edition)**

---

## 2. Intended Use  
This system suggests an optimized ranking of songs from a curated catalog based on a user's exact mood and energy preferences. It assumes that users know precisely what tempo and intensity they want to hear. It is built strictly as a classroom exploration tool to simulate how massive algorithms operate locally, and it is not intended for real-world commercial scale or streaming use without further data scaling.

---

## 3. How the Model Works  
This recommender abandons standard collaborative "who clicked what" logic and relies on purely content-based mathematical filtering. It uses "Genre" as a structural baseline filter (awarding 1.0 points) and "Mood" as a soft affinity boost (also 1.0 points). It then computes the exact numerical distance between the user's requested track characteristics (like Energy and Danceability on a 0-1 scale) and the mathematical audio features mapped in the dataset. By scoring distance, it ensures the songs closest to the target mathematically bubble up to the top!

---

## 4. Data  
The dataset is a lightweight CSV file containing exactly 18 distinct song records. Each record spans highly diverse categories including Pop, Synthwave, Lofi, Classical, Metal, and EDM. The dataset was manually expanded from its original 10 rows to include harsh, adversarial moods (like "Angry" Metal or "Sad" Classical) to artificially test the limits of the math algorithm.

---

## 5. Strengths  
The system is phenomenally accurate at executing "Vibe" matches over raw Genre labels. After adjusting the weights, it successfully prioritizes high-energy tracks for a user who actively wants high-energy music, even if the text genre tags don't perfectly align. It behaves extremely predictably and transparently.

---

## 6. Limitations and Bias 
This recommendation engine exhibits a very rigid "filter bubble" bias directly resulting from how it penalizes "energy gaps." Because our `songs.csv` dataset is currently split between completely extreme high-energy gym anthems and heavily sedated lofi tracks, any user requesting a balanced, moderate-energy profile will automatically be penalized and mathematically alienated by the system. Furthermore, because the algorithm strictly enforces rigid categorical point bonuses for "matching moods," it inherently ignores highly relevant genre-bending tracks that might actually satisfy the user's acoustic desires but happen to be tagged with slightly different text labels.

---

## 7. Evaluation  
I systematically evaluated the engine by running four distinct profile tests: "High-Energy Pop", "Chill Lofi", "Deep Intense Rock", and a logically conflicted "Adversarial" profile (which requested Classical music but with extreme dance club energy levels). 

What strongly surprised me was how frequently the aggressive workout track "Gym Hero" surfaced near the very top of the list for users who just wanted light, breezy "Happy Pop." 

Why does this happen? My algorithm relies heavily on measuring the math of the audio. "Gym Hero" has an extraordinarily high metric for energy. Because the Pop listener also requested high energy, "Gym Hero" acquired massive mathematical points, overpowering the fact that its text mood was listed as "Intense" instead of "Happy". The math engine essentially concluded that the sheer speed and momentum of the track was far more relevant than the subjective text label a human typed into the spreadsheet.

---

## 8. Future Work  
If I kept developing this, I would:
1. Integrate massive Spotify APIs so the raw dataset isn't restricted to 18 rows.
2. Build a user-facing GUI using a framework like Streamlit so users don't have to fiddle with Python dictionaries to set their profiles.
3. Lower the text-bonus points down to +0.25 to make the algorithm almost entirely reliant on the mathematical audio "math" instead of limiting human labels.

---

## 9. Personal Reflection  
My biggest learning moment during this project was realizing that "algorithms" aren't some mystical, unknowable magic; they are just heavily-weighted subtraction formulas disguised behind massive lists. Using AI tools helped tremendously for brainstorming specific formulas and tracking down formatting errors, but I had to intensely double-check the AI whenever we shifted the weight balance to make sure the math actually did what I intended structurally. 

It completely surprised me how genuinely accurate and "real" a tiny 18-song simulation felt. Seeing the math spit out exactly the song I personally wanted proved that real music recommenders (even the giant ones at Spotify) are using basically identical core logic, just scaled to millions of tracks using cloud servers. If I extended this project, I'd definitely incorporate real APIs!
