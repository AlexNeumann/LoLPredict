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

1. [**findLeagues.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#1-findleaguespy) - used to find a collection of player IDs in a given skill group (Gold, Platinum, Diamond etc.) that can then be used to request a history of matches for each player
2. [**convertEpochTime.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#3-convertepochtimepy) - used within other scripts to convert from Epoch time to standard date format. This is important when trying to determine how many days ago a specific match was played
3. [**singleMatchPull.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#2-singlematchpullpy-1st-iteration-for-data-collection) - takes a summoner ID as input and pulls various data points from the last match played by that summoner ID
4. [**groupMatchPull.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#4-groupmatchpullpy-2nd-iteration-for-data-collection) - loops through roughly 2000 Diamond level players and pulls the data of their last match if it was played within the last 24 hours
5. [**infiniteMatchPull.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#5-infinitematchpullpy-most-up-to-date-iteration-for-data-collection) - continuously tracks more than 20,000 Diamond level players and records their match information if they are currently playing in a ranked solo queue match. This script will result in the most accurate and up-to-date data.
6. [**getMatchResult.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#7-process_datapy) - the CSV file created by **process_data.py** is missing an entry for the **Match Outcome** data point because the match is still being played as the data is pulled. In order to fill in these missing entries, this script opens the CSV file and makes API requests to find the match outcome for each matchID.
7. [**process_data.py**](https://github.com/AlexNeumann/LoLPredict/tree/master/Python%20Scripts#6-get_match_resultspy) - uses the CSV file created by **infiniteMatchPull** and reduces the attributes for each match down to ratios between the Blue and Red team averages. 

Contributors
==========

1. Alex Neumann

Release Notes
==========

