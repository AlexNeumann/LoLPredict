Script Overview
=======

**_API Request limit note:_** Some of these scripts originally had time.sleep(x) statements that were used to slow down the execution of the script in order to stay within the API request limits set forth by Riot. After I obtained a higher API limit I deleted most of these statements

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
    - **API Key:** set to your own Riot API key

***

###2. singleMatchPull.py (1st Iteration for data collection)
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
    - **API Key:** set to your own Riot API key

***

###3. convertEpochTime.py
- **Purpose:** Very simple script that converts from Epoch time to standard date format. The [match API endpoint](https://developer.riotgames.com/api/methods#!/1027/3483) returns the **matchCreation** date in Epoch format. Early in the data collection process I wanted to focus only on recently played games and this script is used to determine how many days ago a given match was played. This script itself is also used within the groupMatchPull script.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/convertEpochTime.py)
- **Console output:**
```javascript
Game was played on: 2015-05-11
Todays date: 2015-09-02
Game was played: 114 days ago
This match is too old
```
- **Variables to adjust:** 
    - **s:** set this to equal to the **matchCreation** variable returned by the match API endpoint
    - **API Key:** set to your own Riot API key

***

###4. groupMatchPull.py (2nd Iteration for data collection)
- **Purpose:** After I was able to pull the data for 1 match using the **singleMatchPull** script, I needed to expand it to be able to pull hundreds of matches. In order to do so I needed to find more summonerIDs that I can use to loop through and pull their most recent match. At this point I did not have the **findLeagues** script yet (I came up with the idea for that script at a later date), so I just used summonerIDs from friends that were in the same tier and used the [league](https://developer.riotgames.com/api/methods#!/985/3351) endpoint to find roughly 2000 summonerIDs.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/groupMatchPull.py)
- **Output:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/groupMatchPull_Output.csv)
- **Console output:**
```javascript
Match 0
Player Name:
Player has summoner ID:
Match ID:
Game was played 0 days ago
Basic information for player: 0 - 10 collected
etc..
```
- **Variables to adjust:** 
    - **API Key:** set to your own Riot API key

***

###5. infiniteMatchPull.py (Most Up-to-date Iteration for data collection)
- **Purpose:** This is most up-to-date version of my data collection process. This script makes use of all the Leagues found by the **findLeagues.py** script to track over 20,000 Diamond level players. The biggest difference with this script is that it continuously tracks a large number of players and makes a request to the [current-game](https://developer.riotgames.com/api/methods#!/976) API endpoint to determine if the player is currently playing a ranked solo queue game. If the player is in an active game, then the script records the data for that game. Previously, there was a 1 game lag that caused the returned data to be slightly inaccurate. This is because the data was pulled after the game was played, which means that the players' performance in that game was already added to Riots servers.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/infiniteMatchPull.py)
- **Output:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/infiniteMatchPull_Output.csv)
- **Script Execution Setup:** Looping through 20,000 players and making requests to check if they are in an active game takes quite a while (especially with lower API request limits). For my setup, I split the 20,000 players into 3 different scripts and ran them all at the same time. This means that there will be some duplication of match data, since a player tracked by script **A** could be playing together with a player tracked by script **B** and the game would be recorded by both **A & B**. These duplicates are deleted during the data cleaning process.
- **Script output:** At the beginning of each new loop the script saves a new CSV file. This allows me to look at the data that I have already pulled without interrupting the execution of the script. With 3 scripts running at the same time this results in the following file structure:
```javascript
infiniteMatchPull_Ouput_ScriptA_1.csv
infiniteMatchPull_Ouput_ScriptB_1.csv
infiniteMatchPull_Ouput_ScriptC_1.csv
infiniteMatchPull_Ouput_ScriptA_2.csv
infiniteMatchPull_Ouput_ScriptB_2.csv
infiniteMatchPull_Ouput_ScriptC_2.csv
infiniteMatchPull_Ouput_ScriptA_3.csv
infiniteMatchPull_Ouput_ScriptB_3.csv
infiniteMatchPull_Ouput_ScriptC_3.csv
```
- **Variables to adjust:** 
    - **leagueID:** use the IDs generated by the **findLeagues.py** output and store as many as you want in this variable. The more IDs you store, the more players will be tracked by the script.
    - **API Key:** set to your own Riot API key

***

###6. get_match_results.py
- **Purpose:** The **infiniteMatchPull** script pulls data while the game is still being played. Because of this the **Match Outcome** variable will be left blank since there is no winner yet. This script opens the CSV file created by  **infiniteMatchPull** and makes requests to the [match API endpoint](https://developer.riotgames.com/api/methods#!/1027/3483) and records who actually won the game.
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/get_match_results.py)
- **Output:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/get_match_results_Output.csv)
- **Console output:**
```javascript
Got to iteration: 1     Status Code: 200
Got to iteration: 2     Status Code: 200
Got to iteration: 3     Status Code: 200
Got to iteration: 4     Status Code: 200
```
- **Variables to adjust:** 
    - **API Key:** set to your own Riot API key

***

###7. process_data.py
- **Purpose:** After I collect all my data I am left with 10 rows of data per match, since there is 1 row for each player in a match. In order to start analyzing my data I condense each match down to 1 row. This script finds the difference between the team averages for each attribute and records it. 
- **Script:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/process_data.py)
- **Output:** [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/process_data_output.csv)
- **Variables to adjust:** 
    - **Input File (r):** change this to match the name of the output file created by the **infiniteMatchPull** script
