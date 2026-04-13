# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
