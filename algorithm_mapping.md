# Algorithm Recipe: Mapping the Logic

To build your recommender simulator, we need to define how it evaluates every song against a user's known preference profile. 

## 1. The "Scoring Rule" for Numerical Features

When dealing with numerical features like `energy` or `valence`, a simple "higher is better" rule doesn't work. If a user likes medium-energy songs (e.g., `0.5`), handing them a song with `0.9` energy is a bad recommendation, even though the number is higher.

**The Solution: Distance-Based Scoring**
We need a formula that rewards *closeness*. The smaller the distance between the song's attribute and the user's preference, the higher the score.

**The Math (Absolute Difference Method):**
1. Find the difference: `Distance = AbsoluteValue(User_Target_Energy - Song_Energy)`
2. Invert it into a score: `Score = 1.0 - Distance`

*Example:* 
If your user's target energy is `0.6` and Song A has an energy of `0.7`:
- Distance = `|0.6 - 0.7| = 0.1`
- Score = `1.0 - 0.1 = 0.9` (A very high, strong score!)

## 2. Feature Weights: Genre vs. Mood

Not all features carry the same level of importance. You should apply **weights** (multipliers) to your scores. 

*   **Genre Match (Heavy Weight - e.g., x2.0):** Genre represents a foundational musical structure. If a user only ever listens to Metal, recommending a smooth Jazz song is almost certainly a failure, regardless of how similar the tempo or mood is. Thus, a genre match should award heavy points or act as a strict filter.
*   **Mood Match (Medium Weight - e.g., x1.2):** Mood usually describes the specific emotional application of the song (e.g., 'chill' or 'happy'). While it's important for creating a cohesive playlist, it's slightly more subjective than genre and often naturally correlates with our numerical features (valence and energy).

**Suggested Algorithm Recipe for a single song:**
`Total_Score = (Genre_Match_Score * 2.0) + (Mood_Match_Score * 1.2) + (Energy_Proximity_Score * 1.0) + (Valence_Proximity_Score * 1.0)`

## 3. Scoring Rule vs. Ranking Rule

To build a complete recommendation system, you must have both a Scoring Rule and a Ranking Rule.

*   **The Scoring Rule (Evaluation):** This operates on a **micro-level**. It looks at *one single song* in isolation and compares it against the user's profile to output a mathematical score (e.g., "Song A gets 4.2 points").
*   **The Ranking Rule (Action):** This operates on a **macro-level**. Once every single song in your database has been individually scored, the ranking rule takes that entire list, sorts it in descending order from highest score to lowest score, and decides how many to present to the user (e.g., "Take the top 5 highest-scoring songs and display them as the Discover Weekly playlist").

Without the Scoring Rule, you have no way to evaluate a song's relevance. Without the Ranking Rule, you just have a massive pile of unordered scores with no way to present a curated list to the user.
