# Code Written by: Alex Neumann
# CIS Honors Thesis
# Spring - Fall 2015 - Barrett Honors College

# use 'pip install requests' to get the 'requests' library on your system
import requests
import json
import sys
import time # useful in throttling API requests
import random
import datetime
from datetime import date

# API KEY
APIkey = 'API_KEY_HERE'

# Hold the names of players
validPlayerNames = []

# player = smiling 		league = Vladimir's Maulers
time.sleep(1)
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/20672928?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))

for x in range (0, len(players["20672928"][0]["entries"])):
	try:
		# print(players["20672928"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["20672928"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")

# player = Blooom	league = Kog'Maw's Warlocks
time.sleep(1)		
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/21345869?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		

for x in range (0, len(players["21345869"][0]["entries"])):
	try:
		# print(players["21345869"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["21345869"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")

# player = Pseudonaut		league = Darius's Wizards
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/22802244?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["22802244"][0]["entries"])):
	try:
		# print(players["22802244"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["22802244"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")
		
# player = MisterImpossible		league = Kog'Maw's Horde
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/140126?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["140126"][0]["entries"])):
	try:
		# print(players["140126"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["140126"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")
		
# player = the saddest pimp		league = Heimerdinger's Mercenaries
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/29172059?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["29172059"][0]["entries"])):
	try:
		# print(players["29172059"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["29172059"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")
		
# player = Ugu		league = Teemo's Scouts
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/24079133?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["24079133"][0]["entries"])):
	try:
		# print(players["24079133"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["24079133"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")
		
# player = Haw		league = Miss Fortune's Weaponmasters
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/25055709?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["25055709"][0]["entries"])):
	try:
		# print(players["25055709"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["25055709"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")

# player = Morning Melon		league = Varus's Warmongers
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/20587455?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["20587455"][0]["entries"])):
	try:
		# print(players["20587455"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["20587455"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")
		
# player = Maxim White Gold		league = Jarvan IV's Elite
time.sleep(1)	
validPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/39079486?api_key=" + APIkey)
players = json.loads(validPlayers.content.decode('utf-8'))		
		
for x in range (0, len(players["39079486"][0]["entries"])):
	try:
		# print(players["39079486"][0]["entries"][x]["playerOrTeamName"])
		validPlayerNames.append(players["39079486"][0]["entries"][x]["playerOrTeamName"])
	except:
		print("one entry didnt work")
		
	
#print(len(validPlayerNames))		
player_pool = validPlayerNames

# track names of players that have not played a game within the last 7 days
inactive_pool = []

#track how many pulls I am making
APIpulls = 0
# tracks how many matches were too old for analysis
oldMatches = 0

output = open("groupMatchPull_Output.csv","w")
output.write("Match #, MATCH_ID, Summoner, Summoner_ID, Champion_id, Champion_KDA, P_Champion_winrate, P_Champion_gamesplayed, 3RecentWinrate, 3RecentKDA, Season Games Played, Season Winrate, Season KDA, Side, Highest_Rank, Outcome, Manual Check, Lane, Role, Champion\n")

# loop through player_pool 
#for a in range(0,len(player_pool)):
for a in range(0,2):
	try:
		print("MATCH " + str(a))
		number = a
		# print(number)
		
		#find summoner ID for chosen summoner name
		summonerID = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + player_pool[number] + "?api_key=" + APIkey)
		APIpulls = APIpulls + 1
		#time.sleep(1)
		
		# load json object
		summonerID_data = json.loads(summonerID.content.decode('utf-8'))
		# print(summonerID_data)
		
		# convert chosen summoner name to lowercase and remove all spaces - for json 
		print(player_pool[number])
		name_no_space = player_pool[number].replace(" ", "")
		name_no_space = name_no_space.lower()
		# print(name_no_space)

		# from the json object, retrieve the summonerID
		summoner = summonerID_data[name_no_space]["id"]
		print(player_pool[number] + " has summoner ID: " + str(summoner))
		
		#get match history using the summonerID - only pull the most recent match
		match_history = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+ str(summoner) + "?rankedQueues=RANKED_SOLO_5x5&beginIndex=0&endIndex=1&api_key=" + APIkey)
		match_history_data = json.loads(match_history.content.decode('utf-8'))
		#time.sleep(1)
		
		APIpulls = APIpulls + 1
		
		# Find the matchCreation to determine if the match is recent enough for analysis
		matchCreation = match_history_data["matches"][0]["matchCreation"]
		print(matchCreation)
		#get the match creation time in epoch format
		s = str(matchCreation)
		t = datetime.datetime.fromtimestamp(float(s)/1000.)

		fmt = "%Y-%m-%d %H:%M:%S"
		
		# convert from epoch to date format
		dateOfMatch = t.strftime(fmt)[:10]
		date1 = date(int(dateOfMatch[0:4]), int(dateOfMatch[5:7]), int(dateOfMatch[8:10]))
		
		# get today's date
		today = time.strftime("%Y-%m-%d")
		date2 = date(int(today[0:4]), int(today[5:7]), int(today[8:10]))
		
		# calculate how many days ago the match was played
		delta = date2 - date1
		print("Game was played " + str(delta.days) + " days ago")
		delta = delta.days
		
		# if the match is older than 1 days skip this loop iteration
		if delta >0:
			# skip rest
			oldMatches = oldMatches + 1
			if delta > 7:
				inactive_pool.append(name_no_space)
			print("MATCH " + str(a) + " is too old. Skipping this iteration...")
		else:
			# do rest of loop		
			# Find the matchId for the most recent game in the match history
			match_id = match_history_data["matches"][0]["matchId"]
			print("The match id is: " + str(match_id))
			
			# Pull the match details with the corresponding matchId
			match_results = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(match_id) + "?api_key=" + APIkey)
			match_results_data = json.loads(match_results.content.decode('utf-8'))
		#	time.sleep(1)
			
			APIpulls = APIpulls + 1
			
			# declare all variables that will contain the stats
			
			# name of all players
			playerNames = []
			# summoner IDs of all players
			playerSummonerID = []
			# highest rank from previous season (bronze, silver, gold, platinum, diamond, master, challenger)
			playerHighestPrevRank = []
			# The id of the champion being played by each player
			playerChampion = []
			# did the player win or lose - true/false
			playerMatchOutcome = []
			# what side did the player start on? players 1-5 = Blue, 6-10 = Red
			playerSide = ['Blue','Blue','Blue','Blue','Blue','Red','Red','Red','Red','Red']
			# the players overall Kill Death Assist ratio on the champion they played in the match
			playerChampionKDA = []
			# the total number of games the player has played on a specific champion
			playerChampionGamesPlayed = []
			# overall winrate of the player on a specific champion
			playerChampionWinrate = []
			# total solo queue ranked games played by the player during the current season
			playerTotalSeasonGamesPlayed = []
			# total overall winrate of the player for the current season
			playerTotalSeasonWinrate = []
			# total overall Kill Death Assist ratio for the current season
			playerTotalSeasonKDA = []
			# the player's winrate over the last 3 ranked solo queue matches
			player3RecentWinrate = []
			# the player's Kill Death Assist ratio over the last 3 ranked solo queue matches
			player3RecentKDA = []
			# boolean: temporary variable to check if match history feature is working
			manualCheck = []
			# string: player lane - mid, middle, top, jungle, bot, bottom
			playerLane = []
			# string: player role - duo, none, solo, duo_carry, duo_support
			playerRole = []
			# champion name
			championName = []
			
			for i in range(0,10):
				# get player name
				# playerNames.append(match_results_data["participantIdentities"][i]["player"]["summonerName"])
				# get player Summoner ID
				playerSummonerID.append(match_results_data["participantIdentities"][i]["player"]["summonerId"])
				# get player highest previous rank
				playerHighestPrevRank.append(match_results_data["participants"][i]["highestAchievedSeasonTier"])
				# get champion id that is played
				champID = match_results_data["participants"][i]["championId"]
				playerChampion.append(match_results_data["participants"][i]["championId"])
				# get player outcome, did they win or lose? Ture = win, False = loss
				playerMatchOutcome.append(match_results_data["participants"][i]["stats"]["winner"])
				# get player Lane and Role
				playerLane.append(match_results_data["participants"][i]["timeline"]["lane"])
				# get Role
				playerRole.append(match_results_data["participants"][i]["timeline"]["role"])
				
				Champion = ''
				# Find the champion matching the champion id								
				if champID ==1:
					Champion = 'Annie'
				if champID ==2:
					Champion = 'Olaf'
				if champID ==3:
					Champion = 'Galio'
				if champID ==4:
					Champion = 'Twisted Fate'
				if champID ==5:
					Champion = 'Xin Zhao'
				if champID ==6:
					Champion = 'Urgot'
				if champID ==7:
					Champion = 'LeBlanc'
				if champID ==8:
					Champion = 'Vladimir'
				if champID ==9:	
					Champion = 'Fiddlesticks'
				if champID ==10:	
					Champion = 'Kayle'
				if champID ==11:	
					Champion = 'Master Yi'
				if champID ==12:
					Champion = 'Alistar'
				if champID ==13:
					Champion = 'Ryze'
				if champID ==14:
					Champion = 'Sion'
				if champID ==15:
					Champion = 'Sivir'
				if champID ==16:
					Champion = 'Soraka'
				if champID ==17:
					Champion = 'Teemo'
				if champID ==18:
					Champion = 'Tristana'
				if champID ==19:
					Champion = 'Warwick'
				if champID ==20:
					Champion = 'Nunu'
				if champID ==21:
					Champion = 'Miss Fortune'
				if champID ==22:
					Champion = 'Ashe'
				if champID ==23:
					Champion = 'Tryndamere'
				if champID ==24:
					Champion = 'Jax'
				if champID ==25:
					Champion = 'Morgana'
				if champID ==26:
					Champion = 'Zilean'
				if champID ==27:
					Champion = 'Singed'
				if champID ==28:
					Champion = 'Evelynn'
				if champID ==29:
					Champion = 'Twitch'
				if champID ==30:
					Champion = 'Karthus'
				if champID ==31:
					Champion = 'Cho Gath'
				if champID ==32:
					Champion = 'Amumu'
				if champID ==33:
					Champion = 'Rammus'
				if champID ==34:
					Champion = 'Anivia'
				if champID ==35:
					Champion = 'Shaco'
				if champID ==36:
					Champion = 'Dr. Mundo'
				if champID ==37:
					Champion = 'Sona'
				if champID ==38:
					Champion = 'Kassadin'
				if champID ==39:
					Champion = 'Irelia'
				if champID ==40:
					Champion = 'Janna'
				if champID ==41:
					Champion = 'Gangplank'
				if champID ==42:
					Champion = 'Corki'
				if champID ==43:
					Champion = 'Karma'
				if champID ==44:
					Champion = 'Taric'
				if champID ==45:
					Champion = 'Veigar'
				if champID ==48:
					Champion = 'Trundle'
				if champID ==50:
					Champion = 'Swain'
				if champID ==51:
					Champion = 'Caitlyn'
				if champID ==53:
					Champion = 'Blitzcrank'
				if champID ==54:
					Champion = 'Malphite'
				if champID ==55:
					Champion = 'Katarina'
				if champID ==56:
					Champion = 'Nocturne'
				if champID ==57:
					Champion = 'Maokai'
				if champID ==58:
					Champion = 'Renekton'
				if champID ==59:
					Champion = 'Jarvan IV'
				if champID ==60:
					Champion = 'Elise'
				if champID ==61:
					Champion = 'Orianna'
				if champID ==62:
					Champion = 'Wukong'
				if champID ==63:
					Champion = 'Brand'
				if champID ==64:
					Champion = 'Lee Sin'
				if champID ==67:
					Champion = 'Vayne'
				if champID ==68:
					Champion = 'Rumble'
				if champID ==69:
					Champion = 'Cassiopeia'
				if champID ==72:
					Champion = 'Skarner'
				if champID ==74:
					Champion = 'Heimerdinger'
				if champID ==75:
					Champion = 'Nasus'
				if champID ==76:
					Champion = 'Nidalee'
				if champID ==77:
					Champion = 'Udyr'
				if champID ==78:
					Champion = 'Poppy'
				if champID ==79:
					Champion = 'Gragas'
				if champID ==80:
					Champion = 'Pantheon'
				if champID ==81:
					Champion = 'Ezreal'
				if champID ==82:
					Champion = 'Mordekaiser'
				if champID ==83:
					Champion = 'Yorick'
				if champID ==84:
					Champion = 'Akali'
				if champID ==85:
					Champion = 'Kennen'
				if champID ==86:
					Champion = 'Garen'
				if champID ==89:
					Champion = 'Leona'
				if champID ==90:
					Champion = 'Malzahar'
				if champID ==91:
					Champion = 'Talon'
				if champID ==92:
					Champion = 'Riven'
				if champID ==96:
					Champion = 'Kog Maw'
				if champID ==98:
					Champion = 'Shen'
				if champID ==99:
					Champion = 'Lux'
				if champID ==101:
					Champion = 'Xerath'
				if champID ==102:
					Champion = 'Shyvana'
				if champID ==103:
					Champion = 'Ahri'
				if champID ==104:
					Champion = 'Graves'
				if champID ==105:
					Champion = 'Fizz'
				if champID ==106:
					Champion = 'Volibear'
				if champID ==107:
					Champion = 'Rengar'
				if champID ==110:
					Champion = 'Varus'
				if champID ==111:
					Champion = 'Nautilus'
				if champID ==112:
					Champion = 'Viktor'
				if champID ==113:
					Champion = 'Sejuani'
				if champID ==114:
					Champion = 'Fiora'
				if champID ==115:
					Champion = 'Ziggs'
				if champID ==117:
					Champion = 'Lulu'
				if champID ==119:
					Champion = 'Draven'
				if champID ==120:
					Champion = 'Hecarim'
				if champID ==121:
					Champion = 'Kha Zix'
				if champID ==122:
					Champion = 'Darius'
				if champID ==126:
					Champion = 'Jayce'
				if champID ==127:
					Champion = 'Lissandra'
				if champID ==131:
					Champion = 'Diana'
				if champID ==133:
					Champion = 'Quinn'
				if champID ==134:
					Champion = 'Syndra'
				if champID ==143:
					Champion = 'Zyra'
				if champID ==150:
					Champion = 'Gnar'
				if champID ==154:
					Champion = 'Zac'
				if champID ==157:
					Champion = 'Yasuo'
				if champID ==161:
					Champion = 'Vel Koz'
				if champID ==201:
					Champion = 'Braum'
				if champID ==222:
					Champion = 'Jinx'
				if champID ==236:
					Champion = 'Lucian'
				if champID ==238:
					Champion = 'Zed'
				if champID ==245:
					Champion = 'Ekko'
				if champID ==254:
					Champion = 'Vi'
				if champID ==266:
					Champion = 'Aatrox'
				if champID ==267:
					Champion = 'Nami'
				if champID ==268:
					Champion = 'Azir'
				if champID ==412:
					Champion = 'Thresh'
				if champID ==421:
					Champion = 'Rek Sai'
				if champID ==429:
					Champion = 'Kalista'
				if champID ==432:
					Champion = 'Bard'
				if champID ==233:
					Champion = 'Tahm Kench'
				print(champID)
				print(Champion)
				championName.append(Champion)
						
				print("Basic information for player: " + str(i) + " collected...")
			print(playerMatchOutcome)
			
			# loop through all 10 players and get their KDA on the champion they played. Current season only
			# using: stats-v1.3 API
			for g in range (0,10):
				print("----------- Starting Data Collection for player: " + str(g) + " -----------")
				print("")
				#time.sleep(1)
				playerStats = requests.get("https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/" + str(playerSummonerID[g]) + "/ranked?season=SEASON2015&api_key=" + APIkey)
				playerStatsData = json.loads(playerStats.content.decode('utf-8'))
				
				APIpulls = APIpulls + 1
				
				assist = 0
				kills = 0
				deaths = 0
				gamesPlayedOnChamp = 0
				gamesWonOnChamp = 0 
				gamesLostOnChamp = 0
				
				# go through the summary stats and calculate the KDA for the champion
				# also record the number of games the player has played on that champion
				for x in range (0, len(playerStatsData["champions"])):
					if playerStatsData["champions"][x]["id"] == playerChampion[g]:
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
				print("Stats for player: " + str(g) + " collected...")
				
				# request recent match history for each player 
				# used to calculate last 3 game winrate and KDA
			    #	time.sleep(2)
				# beginIndex = 1; endIndex = 15; in order to get the 3 games prior to most recent one
				playerHistory = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+ str(playerSummonerID[g]) + "?rankedQueues=RANKED_SOLO_5x5&beginIndex=0&endIndex=15&api_key=" + APIkey)
				playerHistory_data = json.loads(playerHistory.content.decode('utf-8'))
				
				APIpulls = APIpulls + 1
				
				# tracks if the match is located within the 15 most recent matches of the match_history data
				available = -100
				
				# find the correct match within the match history 
				for d in range(0,15):
					if playerHistory_data["matches"][d]["matchId"] == match_id:
						available = d 
				
				past3Kills = 0
				past3Deaths = 0
				past3Assists = 0
				past3Wins = 0
				
				# if 'available' is larger than 2, then all the data we need is found in the playerHistory_data variable
				if available > 2:
					print("All data was available in the 1st match history pull.")
					for y in range(1,4):
						if str(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["winner"]) == 'True':
							past3Wins = past3Wins + 1
						# print(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["winner"])
						# print(str(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["winner"]))
						past3Kills = past3Kills + int(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["kills"])
						past3Deaths = past3Deaths + int(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["deaths"])
						past3Assists = past3Assists + int(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["assists"])
				
					past3Winrate = 0
					past3kda = 0
					
					if past3Kills == 0 and past3Deaths == 0 and past3Assists == 0:
						past3kda = 0.00
					elif past3Deaths == 0:
						past3kda = round((past3Kills + past3Assists)/(1), 2)
					else:
						past3kda = round((past3Kills + past3Assists)/(past3Deaths), 2)
					
					past3Winrate = round((past3Wins/3),4) * 100
					
					player3RecentWinrate.append(past3Winrate)
					player3RecentKDA.append(past3kda)
					manualCheck.append('no')
				# if 'available' is still set to 100, then the matchID was not found in the history, and we need to pull more matches
				elif available == -100:
					print("A 2nd match history pull was needed.")
					# we can overwrite these variables since none of the data we need is located in them
					# change the beginIndex to 15 and endIndex to 30 to pull the next 15 matches
				#	time.sleep(1)
					playerHistory = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+ str(playerSummonerID[g]) + "?rankedQueues=RANKED_SOLO_5x5&beginIndex=15&endIndex=30&api_key=" + APIkey)
					playerHistory_data = json.loads(playerHistory.content.decode('utf-8'))
					
					
					APIpulls = APIpulls + 1
					
					# now we go through and perform the same check to see if the matchID is found in here and the 3 games prior to that one are in range
					available2 = -100
					for e in range(0,15):
						if playerHistory_data["matches"][e]["matchId"] == match_id:
							available2 = e 
						
					# if available2 is greater than 2, then we have all the data we need
					if available2 > 2:
						for y in range(1,4):
							if str(playerHistory_data["matches"][available2 - y]["participants"][0]["stats"]["winner"]) == 'True':
								past3Wins = past3Wins + 1
							# print(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["winner"])
							# print(str(playerHistory_data["matches"][available - y]["participants"][0]["stats"]["winner"]))
							past3Kills = past3Kills + int(playerHistory_data["matches"][available2 - y]["participants"][0]["stats"]["kills"])
							past3Deaths = past3Deaths + int(playerHistory_data["matches"][available2 - y]["participants"][0]["stats"]["deaths"])
							past3Assists = past3Assists + int(playerHistory_data["matches"][available2 - y]["participants"][0]["stats"]["assists"])
					
						past3Winrate = 0
						past3kda = 0
						
						if past3Kills == 0 and past3Deaths == 0 and past3Assists == 0:
							past3kda = 0.00
						elif past3Deaths == 0:
							past3kda = round((past3Kills + past3Assists)/(1), 2)
						else:
							past3kda = round((past3Kills + past3Assists)/(past3Deaths), 2)
						
						past3Winrate = round((past3Wins/3),4) * 100
						
						player3RecentWinrate.append(past3Winrate)
						player3RecentKDA.append(past3kda)	
						manualCheck.append('no')
					else:
						print("The second match history pull was not enough... should enter -100")
						past3Winrate = -100
						past3kda = -100
						player3RecentWinrate.append(past3Winrate)
						player3RecentKDA.append(past3kda)
						manualCheck.append('no')
				elif available < 3:
					# calculate how many matches I need from the second match history
					# if 'available' = 2, then I need 1 match from the second history
					extra = 3 - available
					print("Data was between first and second history pull... calculating..")
					# 'available' can be = 0, 1, 2 
					# if 'available is = 2, we need games 1, 0 and the most recent one from the second call
					
					# make the second call
				#	time.sleep(1)
					playerHistory = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+ str(playerSummonerID[g]) + "?rankedQueues=RANKED_SOLO_5x5&beginIndex=15&endIndex=30&api_key=" + APIkey)
					playerHistory_data2 = json.loads(playerHistory.content.decode('utf-8'))
					
					APIpulls = APIpulls + 1
					
					# get the partial data from the first pull
					for n in range(0,available):
						if str(playerHistory_data["matches"][n]["participants"][0]["stats"]["winner"]) == 'True':
								past3Wins = past3Wins + 1
						past3Kills = past3Kills + int(playerHistory_data["matches"][n]["participants"][0]["stats"]["kills"])
						past3Deaths = past3Deaths + int(playerHistory_data["matches"][n]["participants"][0]["stats"]["deaths"])
						past3Assists = past3Assists + int(playerHistory_data["matches"][n]["participants"][0]["stats"]["assists"])
					# get the other partial data from the second pull
					for m in range(0, extra):
						if str(playerHistory_data2["matches"][14 - m]["participants"][0]["stats"]["winner"]) == 'True':
								past3Wins = past3Wins + 1
						past3Kills = past3Kills + int(playerHistory_data2["matches"][14 - m]["participants"][0]["stats"]["kills"])
						past3Deaths = past3Deaths + int(playerHistory_data2["matches"][14 - m]["participants"][0]["stats"]["deaths"])
						past3Assists = past3Assists + int(playerHistory_data2["matches"][14 - m]["participants"][0]["stats"]["assists"])
					
					past3Winrate = 0
					past3kda = 0
					
					if past3Kills == 0 and past3Deaths == 0 and past3Assists == 0:
						past3kda = 0.00
					elif past3Deaths == 0:
						past3kda = round((past3Kills + past3Assists)/(1), 2)
					else:
						past3kda = round((past3Kills + past3Assists)/(past3Deaths), 2)
					
					past3Winrate = round((past3Wins/3),4) * 100
					
					player3RecentWinrate.append(past3Winrate)
					player3RecentKDA.append(past3kda)	
					manualCheck.append('yes')					
				
				else:
					print("Something went wrong... should enter -200")
					past3Winrate = -200
					past3kda = -200
					player3RecentWinrate.append(past3Winrate)
					player3RecentKDA.append(past3kda)	
				
				# print("Recent winrate / kda information for player: " + str(i) + " collected...")
				print("")
				print("----------- Ending Data Collection for player: " + str(g) + "   -----------")
				print("")
			# write data to file with this format:
			# MATCH_ID, Summoner, Summoner_ID, Champion_id, Champion_KDA, P_Champion_winrate, P_Champion_gamesplayed, 
			# 3RecentWinrate, 3RecentKDA, Season Games Played, Season Winrate, Season KDA, Side, Highest_Rank, Match_KDA, Outcome

			playerNames = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10']
			matchNum = [str(a),str(a),str(a),str(a),str(a),str(a),str(a),str(a),str(a),str(a)]
			
			for f in range (0,10):
				output.write(str(matchNum[f]) + ", "
				+ str(match_id) + ", "
				+ playerNames[f] + "," 
				+ str(playerSummonerID[f]) + ", " 
				+ str(playerChampion[f]) + ", " 
				+ str(playerChampionKDA[f]) + ", " 
				+ str(playerChampionWinrate[f]) + ", "
				+ str(playerChampionGamesPlayed[f]) + ", "
				+ str(player3RecentWinrate[f]) + ", "
				+ str(player3RecentKDA[f]) + ", "
				+ str(playerTotalSeasonGamesPlayed[f]) + ", "
				+ str(playerTotalSeasonWinrate[f]) + ", "
				+ str(playerTotalSeasonKDA[f]) + ", "
				+ playerSide[f] + ", " 
				+ playerHighestPrevRank[f] + ", " 
				+ str(playerMatchOutcome[f]) + ", "
				+ str(manualCheck[f]) + ", "
				+ str(playerLane[f]) + ", "
				+ str(playerRole[f]) + ", "
				+ str(championName[f]))
				output.write("\n")
			print("waiting 3 seconds before starting next iteration...")
		#	time.sleep(3)	
			print("Total api pulls = " + str(APIpulls))
		
	except:
		# something went wrong so just place '?' for this match
		matchNum = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		match_id = '?'
		playerNames = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerSummonerID = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerHighestPrevRank = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerChampion = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerMatchOutcome = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerSide = ['?','?','?','?','?','?','?','?','?','?']
		playerChampionKDA = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerChampionGamesPlayed = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerChampionWinrate = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerTotalSeasonGamesPlayed = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerTotalSeasonWinrate = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerTotalSeasonKDA = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		player3RecentWinrate = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		player3RecentKDA = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		manualCheck = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerLane = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		playerRole = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
		championName = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']

		for f in range (0,10):
			output.write(str(matchNum[f]) + ", "
			+ str(match_id) + ", "
			+ playerNames[f] + "," 
			+ str(playerSummonerID[f]) + ", " 
			+ str(playerChampion[f]) + ", " 
			+ str(playerChampionKDA[f]) + ", " 
			+ str(playerChampionWinrate[f]) + ", "
			+ str(playerChampionGamesPlayed[f]) + ", "
			+ str(player3RecentWinrate[f]) + ", "
			+ str(player3RecentKDA[f]) + ", "
			+ str(playerTotalSeasonGamesPlayed[f]) + ", "
			+ str(playerTotalSeasonWinrate[f]) + ", "
			+ str(playerTotalSeasonKDA[f]) + ", "
			+ playerSide[f] + ", " 
			+ playerHighestPrevRank[f] + ", " 
			+ str(playerMatchOutcome[f]) + ", "
			+ str(manualCheck[f]) + ", "
			+ str(playerLane[f]) + ", "
			+ str(playerRole[f]) + ", "
			+ str(championName[f]))
			output.write("\n")
		time.sleep(3)
output.write("#oldMatches: " + str(oldMatches))
output.write("\n")

inactive = ''

for u in range(0, len(inactive_pool)):
	inactive = inactive + "," + inactive_pool[u]
output.write(inactive)
# print the total runtime of the script on screen (used to calculate rate limit for API requests)
# print(datetime.now() - startTime)
print("Total api pulls = " + str(APIpulls))