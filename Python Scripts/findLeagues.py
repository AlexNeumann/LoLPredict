#######################################################################
##																	 ##
##						Code Written by: Alex Neumann				 ##
##							CIS Honors Thesis						 ##
##				Spring - Fall 2015	Barrett Honors College			 ##
##																	 ##
#######################################################################

import requests
import json
import random
import datetime

# Riot API key -
APIkey = 'API_KEY_HERE'

# Summoner ID of a player in the requested skill level (Diamond, Plat, Gold, Silver...)
# Summoner name = smiling, ID = 20672928
nextID = 20672928
tier = "DIAMOND"

# number of leagues you want to find (avg. division player size = 200)
league_num = 40

leagueNames = []
leaguePlayerID = []
leagueDivision = []

leaguesFound = 0

# create a new CSV file that will store the league information
output = open("DiamondLeagues1.csv","w")

# column headers for the CSV file
output.write("LeagueName, PlayerID, Division\n")

try:	
	# Loop until the entered number of leagues has been found
	while(leaguesFound < league_num):	
		try:
			playerName = []
			playerID = []
			
			# generate an int between 1 and 5 to randomize which game from the history will be used
			# this avoids the 'spidertrap' issue
			mh_number = random.randint(0,8)
			mh_number1 = mh_number + 1
			# get the next players match history
			playerHistory = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/" + str(nextID) + "?rankedQueues=RANKED_SOLO_5x5&beginIndex=" + str(mh_number) + "&endIndex=" + str(mh_number1) + "&api_key=" + APIkey)
			playerHistory_data = json.loads(playerHistory.content.decode('utf-8'))					
			
			# get the match ID and then use it to call the MatchAPI to find the 10 players in that match
			matchID = playerHistory_data["matches"][0]["matchId"]
			match = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(matchID) + "?api_key=" + APIkey)
			match_data = json.loads(match.content.decode('utf-8'))
			
			# loop through the match participants and store their names and IDs
			for a in range (0,10):
				playerName.append(match_data["participantIdentities"][a]["player"]["summonerName"])
				playerID.append(match_data["participantIdentities"][a]["player"]["summonerId"])
			
			# generate random int between 1 and 10 to use as the nextID
			number = random.randint(0,9)
			
			# use the generated int to store the ID used in the next loop iteration
			nextID = playerID[number]
			
			#print(playerName)
			# use the 10 new IDs to lookup what League they are in
			for b in range (0,10):
				playerLeague = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/" + str(playerID[b]) + "?api_key=" + APIkey)
				playerLeague_data = json.loads(playerLeague.content.decode('utf-8'))
				
				# if the player is in a Diamond league and we have not recorded it yet, add it to our list of leagues
				if (playerLeague_data[str(playerID[b])][0]["tier"] == tier and playerLeague_data[str(playerID[b])][0]["name"] not in leagueNames):
					leagueNames.append(playerLeague_data[str(playerID[b])][0]["name"])
					leaguePlayerID.append(playerID[b])
					leagueDivision.append(playerLeague_data[str(playerID[b])][0]["tier"])
					
					numberofplayers = len(playerLeague_data[str(playerID[b])][0]["entries"])
					
					leaguesFound = leaguesFound + 1
					print("I found a total of: " + str(leaguesFound) + " leagues..." + "Size: " + str(numberofplayers))
		except:
			print("error")
# allows me to interrupt the script with CTRL-C to break the while loop and write the data to the file
except KeyboardInterrupt:
	pass
		
# write output to file once all leagues have been found		
for f in range (0,len(leagueNames)):
	output.write(str(leagueNames[f]) + ", "
	+ str(leaguePlayerID[f]) + ", "
	+ str(leagueDivision[f]))
	output.write("\n")
			
			
			
			
			
			
			
			
			
			
			
			