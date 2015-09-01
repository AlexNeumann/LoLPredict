# LoLPredict


Overview 
=======

**This repository stores various Python scripts that can be used to make API requests to the 
Riot Games League of Legends API. This is part of an undergraduate thesis project focusing on predicting the outcome
of ranked solo queue matches in the game League of Legends.**

**Live Demo (BETA):** 

Python Script Summary
==========

Below is a brief summary of all Python scripts and what they are used for. More detail on each script is provided within the scripts folder.

1. **findLeagues.py** - used to find a collection of player IDs in a given skill group (Gold, Platinum, Diamond etc.) that can then be used to request a history of matches for each player
2. **convertEpochTime.py** - used within other scripts to convert from Epoch time to standard date format. This is important when trying to determine how many days ago a specific match was played
3. **singleMatchPull.py** - takes a summoner ID as input and pulls various data points from the last match played by that summoner ID
4. **groupMatchPull.py** - loops through roughly 2000 Diamond level players and pulls the data of their last match if it was played within the last 24 hours
5. **infiniteMatchPull.py** - continuously tracks more than 20,000 Diamond level players and records their match information if they are currently playing in a ranked solo queue match. This script will result in the most accurate and up-to-date data.


Contributors
==========

1. Alex Neumann

Release Notes
==========

