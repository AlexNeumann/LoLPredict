# Code Written by: Alex Neumann
# CIS Honors Thesis
# Spring - Fall 2015 - Barrett Honors College

import requests
import json
import csv
import time

# Riot API key -
APIkey = 'API_KEY_HERE'

# open our csv
r = csv.reader(open("infiniteMatchPull_OUTPUT_FILE_HERE.csv"))

# skip the first line
skip_first_line = next(r)

# create a new CSV file that will store the league information
output = open("infiniteMatchPull_MatchOutcomeData.csv","w")
# column headers for the CSV file
output.write("MatchID, Outcome, MatchType, FirstTower, FirstBlood, FirstDragon, FirstInhibitor\n")

for x in range(0,10000):
	line = next(r)
	matchID = line[1]
	match_results = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(matchID) + "?api_key=" + APIkey)
	#print("Status Code: " + str(match_results.status_code))
	if str(match_results.status_code) != '200':
		print("error occured")
		outcome = "error"
		type = "error"
		firstTower = "error"
		firstBlood = "error"
		firstDragon = "error"
		firstInhibitor = "error"
	else:
		match_results_data = json.loads(match_results.content.decode('utf-8'))
		print("Got to iteration:" + str(x) + "    Status Code: " + str(match_results.status_code))
		firstTower = str(match_results_data["teams"][0]["firstTower"])	
		firstBlood = str(match_results_data["teams"][0]["firstBlood"])
		firstDragon = str(match_results_data["teams"][0]["firstDragon"])
		firstInhibitor = str(match_results_data["teams"][0]["firstInhibitor"])
		
		
		if firstTower == 'False':
			firstTower = 'Red'
		else:
			firstTower = 'Blue'
		if firstBlood == 'False':
			firstBlood = 'Red'
		else:
			firstBlood = 'Blue'
		if firstDragon == 'False':
			firstDragon = 'Red'
		else:
			firstDragon = 'Blue'
		if firstInhibitor == 'False':
			firstInhibitor = 'Red'
		else:
			firstInhibitor = 'Blue'
		
		print("First tower: " + str(firstTower))
		
		winner = match_results_data["participants"][0]["stats"]["winner"]
		type = match_results_data["queueType"]
		
		outcome = ''
		if str(winner) == "True":
			outcome = "Blue"
		elif str(winner) == "False":
			outcome = "Red"
		else:
			# something went wrong
			outcome = "Yellow"
		
	output.write(str(matchID) + "," + str(outcome) + "," + str(type) + "," + str(firstTower)+ "," + str(firstBlood)+ "," + str(firstDragon)+ "," + str(firstInhibitor))
	output.write("\n")


			
			