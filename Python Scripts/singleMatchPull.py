# Code Written by: Alex Neumann
# CIS Honors Thesis
# Spring - Fall 2015 - Barrett Honors College

# use 'pip install requests' to get the 'requests' library on your system
import requests
import json
import time # useful in throttling API requests

APIkey = 'API_KEY_HERE'
	
# create a new CSV file
output = open("singleMatchPull_output.csv","w")
output.write("MATCH_ID, Summoner, Summoner_ID, Champion_id, Champion_KDA, P_Champion_winrate, P_Champion_gamesplayed, Season Games Played, Season Winrate, Season KDA, Side, Highest_Rank, Match_KDA, Outcome\n")

#summoner name = smiling 		summonerId = 20672928
myID = 20672928

# pull my own MatchList
matchList = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/" + str(myID) + "?rankedQueues=RANKED_SOLO_5x5&seasons=SEASON2015&beginIndex=0&endIndex=1&api_key=" + APIkey)
matchList_data = json.loads(matchList.content.decode('utf-8'))
print(matchList_data)
# Find the matchId for the most recent game in the match history
match_id = matchList_data["matches"][0]["matchId"]
print("MatchId = " + str(match_id))

# Pull the match details with the corresponding matchId
match_results = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(match_id) + "?api_key=" + APIkey)
match_results_data = json.loads(match_results.content.decode('utf-8'))

# NOTES:
# ParticipantId 1-5 are on blue side
# ParticipantId 6-10 are on red side

# Pull the following data from the match:
playerNames = []
playerSummonerID = []
playerKDA = []
playerHighestPrevRank = []
playerChampion = []
playerMatchOutcome = []
playerSide = ['Blue','Blue','Blue','Blue','Blue','Red','Red','Red','Red','Red']
playerChampionKDA = []
playerChampionGamesPlayed = []
playerChampionWinrate = []
playerTotalSeasonGamesPlayed = []
playerTotalSeasonWinrate = []
playerTotalSeasonKDA = []
player3RecentWinrate = []
player3RecentKDA = []

for i in range(0,10):
	# get player name
	playerNames.append(match_results_data["participantIdentities"][i]["player"]["summonerName"])
	# get player Summoner ID
	playerSummonerID.append(match_results_data["participantIdentities"][i]["player"]["summonerId"])
	# get player highest previous rank
	playerHighestPrevRank.append(match_results_data["participants"][i]["highestAchievedSeasonTier"])
	# get champion id that is played
	playerChampion.append(match_results_data["participants"][i]["championId"])
	# get player Kill/Death/Assist ratio for current game
	assist = match_results_data["participants"][i]["stats"]["assists"]
	deaths = match_results_data["participants"][i]["stats"]["deaths"]
	kills = match_results_data["participants"][i]["stats"]["kills"]
	
	if deaths == 0:
		kda = round((kills + assist)/(1), 2)
	else:
		kda = round((kills + assist)/(deaths), 2)
	playerKDA.append(kda)
	# get player outcome, did they win or lose? Ture = win, False = loss
	playerMatchOutcome.append(match_results_data["participants"][i]["stats"]["winner"])
	print("Basic information for player: " + str(i) + " collected...")
	
	
# loop through all 10 players and get their KDA on the champion they played. Current season only
# using: stats-v1.3 API
for i in range (0,10):
	time.sleep(1)
	playerStats = requests.get("https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/" + str(playerSummonerID[i]) + "/ranked?season=SEASON2015&api_key=" + APIkey)
	playerStatsData = json.loads(playerStats.content.decode('utf-8'))
	
	assist = 0
	kills = 0
	deaths = 0
	gamesPlayedOnChamp = 0
	gamesWonOnChamp = 0 
	gamesLostOnChamp = 0
	
	# go through the summary stats and calculate the KDA for the champion
	# also record the number of games the player has played on that champion
	for x in range (0, len(playerStatsData["champions"])):
		if playerStatsData["champions"][x]["id"] == playerChampion[i]:
			assist = playerStatsData["champions"][x]["stats"]["totalAssists"]
			kills = playerStatsData["champions"][x]["stats"]["totalChampionKills"]
			deaths = playerStatsData["champions"][x]["stats"]["totalDeathsPerSession"]			
			gamesPlayedOnChamp = playerStatsData["champions"][x]["stats"]["totalSessionsPlayed"]
			gamesWonOnChamp = playerStatsData["champions"][x]["stats"]["totalSessionsWon"]
			gamesLostOnChamp = playerStatsData["champions"][x]["stats"]["totalSessionsLost"]
	
	if gamesPlayedOnChamp == 0 and gamesWonOnChamp == 0 and gamesLostOnChamp == 0:
		champ_winrate = 'none'
		gamesLostOnChamp = 'none'
		gamesWonOnChamp = 'none'
		gamesPlayedOnChamp = 'none'
	else:
		champ_winrate = round((gamesWonOnChamp/gamesPlayedOnChamp),4) * 100
		
	# total games played this season
	# total winrate this season
	# total KDA this season
	totalSeasonGames = 0
	totalSeasonGamesWon = 0
	seasonDeaths = 0
	seasonAssists = 0
	seasonKills = 0
	
	for m in range (0, len(playerStatsData["champions"])):
		if playerStatsData["champions"][m]["id"] == 0:
			totalSeasonGames = playerStatsData["champions"][m]["stats"]["totalSessionsPlayed"]
			totalSeasonGamesWon = playerStatsData["champions"][m]["stats"]["totalSessionsWon"]
			seasonDeaths = playerStatsData["champions"][m]["stats"]["totalDeathsPerSession"]
			seasonAssists = playerStatsData["champions"][m]["stats"]["totalAssists"]
			seasonKills = playerStatsData["champions"][m]["stats"]["totalChampionKills"]
			
	# calculate season KDA
	if seasonDeaths == 0 and seasonAssists == 0 and seasonKills == 0:
		seasonKDA = 0.00
	elif seasonDeaths == 0:
		seasonKDA = round((seasonKills + seasonAssists)/(1), 2)
	else:
		seasonKDA = round((seasonKills + seasonAssists)/(seasonDeaths), 2)
		
	# add season KDA to array
	playerTotalSeasonKDA.append(seasonKDA)
			
	# add season winrate to array
	totalSeasonWinrate = round((totalSeasonGamesWon/totalSeasonGames),4) * 100
	playerTotalSeasonWinrate.append(totalSeasonWinrate)
	

	playerTotalSeasonGamesPlayed.append(totalSeasonGames)
	playerChampionGamesPlayed.append(gamesPlayedOnChamp)
	playerChampionWinrate.append(champ_winrate)
	
	# calculate champion KDA
	if deaths == 0 and assist == 0 and kills == 0:
		champ_kda = 0.00
	elif deaths == 0:
		champ_kda = round((kills + assist)/(1), 2)
	else:
		champ_kda = round((kills + assist)/(deaths), 2)
		
	playerChampionKDA.append(champ_kda)	
	print("Stats for player: " + str(i) + " collected...")
	
	

# write data to file with this format:
for i in range (0,10):
	output.write(str(match_id) + ", " 
	+ playerNames[i] + "," 
	+ str(playerSummonerID[i]) + ", " 
	+ str(playerChampion[i]) + ", " 
	+ str(playerChampionKDA[i]) + ", " 
	+ str(playerChampionWinrate[i]) + ", "
	+ str(playerChampionGamesPlayed[i]) + ", "
	+ str(playerTotalSeasonGamesPlayed[i]) + ", "
	+ str(playerTotalSeasonWinrate[i]) + ", "
	+ str(playerTotalSeasonKDA[i]) + ", "
	+ playerSide[i] + ", " 
	+ playerHighestPrevRank[i] + ", " 
	+ str(playerKDA[i]) + ", " 
	+ str(playerMatchOutcome[i]))
	output.write("\n")

