Script Overview
=======

###1. findLeagues.py
- Purpose: The [current-game](https://developer.riotgames.com/api/methods#!/976/3336) API endpoint requires a valid summonerID as parameter. Players of the same skill level (Diamond, Platinum, Gold...) are split into different "Leagues" that have unique names. For example, my own "League" is called **Vladimir's Maulers** and includes players from Diamond I through Diamond V. The easiest way to find a large number of summonerIDs in the same skill level is to find the ID of one player within these Leagues and then make a request to the [league](https://developer.riotgames.com/api/methods#!/985/3351) endpoint to find the summonerID of every player within that league.
- Script:[shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/findLeagues.py)
- Output: [shortcut](https://github.com/AlexNeumann/LoLPredict/blob/master/Python%20Scripts/findLeagues_Output.csv)
- Console output:
```javascript
I found a total of: 1 leagues... Size: 201
I found a total of: 2 leagues... Size: 247
I found a total of: 3 leagues... Size: 203  
```

    

