# Profile Evaluations & Output Comparisons

### High-Energy Pop vs. Chill Lofi
**What Changed:** The engine perfectly inverted its results. Fast pop anthems ("Sunrise City") dominated the first test, while slow acoustic tracks ("Library Rain") dominated the second test entirely.
**Why It Makes Sense:** The High-Energy Pop profile specifically requested an energy level of `0.90`, while the Lofi profile specifically targeted `0.35`. The algorithm mathematically penalized down-tempo songs in the first test for being "too slow," but radically rewarded them in the second test for achieving the required calm vibe.

### Chill Lofi vs. Deep Intense Rock
**What Changed:** The top results shifted dramatically from relaxed organic beats to aggressive electric structures ("Storm Runner"). 
**Why It Makes Sense:** Rather than merely relying on the `genre` text match, the algorithm was actively calculating distance against the quantitative attributes. Deep Rock demands a `0.95` energy target. Therefore, any track that dominated the Lofi test mathematically plummeted in the Rock test because the "energy distance gap" was far too enormous to overcome.

### High-Energy Pop vs. The Adversarial Profile
**What Changed:** The adversarial user explicitly requested "Classical" and "Sad" music, yet high-energy pop and dance tracks like "Gym Hero" still ruthlessly flooded the top results. 
**Why It Makes Sense:** During our data experiment, we deliberately halved the value of text labels and doubled the value of the raw numbers. Because the user demanded a physically impossible `0.99` energy level for sad classical music, the system realized no classical songs were fast enough. Instead, it algorithmically surfaced Pop/EDM tracks that delivered the physical momentum the user requested, proving that a purely mathematical "vibe check" can successfully overpower restrictive human text categorization!
