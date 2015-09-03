Script Overview
=======

###1. findLeagues.py
- **Purpose:** The [current-game](https://developer.riotgames.com/api/methods#!/976/3336) API endpoint requires a valid summonerID as parameter. Players of the same skill level (Diamond, Platinum, Gold...) are split into different "Leagues" that have unique names. For example, my own "League" is called **Vladimir's Maulers** and includes players from Diamond I through Diamond V. The easiest way to find a large number of summonerIDs in the same skill level is to find the ID of one player within these Leagues and then make a request to the [league](https://developer.riotgames.com/api/methods#!/985/3351) endpoint to find the summonerID of every player within that league.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/findLeagues.py)
- **Output:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/findLeagues_Output.csv)
- **Console output:**
```javascript
I found a total of: 1 leagues... Size: 201
I found a total of: 2 leagues... Size: 247
I found a total of: 3 leagues... Size: 203  
```
- **Variables that can be changed:** 
    - **nextID:** set this to any valid summoner ID of a player in skill group you want to find
    - **tier:** set this equal to the skill level you want to find ("DIAMOND","GOLD","SILVER" etc.)
    - **league_num:** set this equal to the total number of leagues you want to find. Each league will have an average of 200 summonerIDs. Default is 40 leagues, which results in roughly 8,000 summoner IDs

***

###2. singleMatchPull.py
- **Purpose:** This was the first script I wrote for the project. The main purpose was to learn Python, how to make API requests and how to navigate to the correct attributes within the returned JSON object. This script will pull data for the last game played by a given summoner.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/singleMatchPull.py)
- **Output:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/singleMatchPull_output.csv)
- **Console output:**
```javascript
MatchId = 1937318097
Basic information for player: 0 - 10 collected...
Stats for player: 0 - 10 collected...
Recent winrate / kda information for player: 0 - 10 collected...
```
- **Variables to adjust:** 
    - **myID:** set this to any valid summoner ID for which you want to pull the most recent match. As default it is set to my own summonerID

***

###3. convertEpochTime.py
- **Purpose:** Very simple script that converts from Epoch time to standard date format. The [match API endpoint](https://developer.riotgames.com/api/methods#!/1027/3483) returns the **matchCreation** date in Epoch format. Early in the data collection process I wanted to focus only on recently played games and this script is used to determine how many days ago a given match was played. This script itself is also used within the groupMatchPull script.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/convertEpochTime.py)
- **Console output:**
```javascript
Game was played on: 2015-05-11
Today's date: 2015-09-02
Game was played: 114 days ago
This match is too old
```
- **Variables to adjust:** 
    - **s:** set this to equal to the **matchCreation** variable returned by the match API endpoint
