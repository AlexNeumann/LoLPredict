# Code Written by: Alex Neumann
# CIS Honors Thesis
# Spring - Fall 2015 - Barrett Honors College

import csv

# file name containing all data pulled from API
r = csv.reader(open("infiniteMatchPull_OUTPUT_FILE_HERE.csv"))

# file name of the output
output = open("infiniteMatchPull_Output_Processed.csv","w")

# column headers
output.write("MatchNum, MatchID, ChampionKDA, ChampionWinrate, ChampionGamesPlayed, ChampionPlayrate, PlayrateFlag, SeasonGamesPlayed, SeasonWinrate, SeasonKDA, DamageTypeDiff, rA_kills, rA_assists, rA_deaths, rA_KDA, rA_winrate, rA_gpm, rA_timeToWin, rA_totalDmgToChamp, rA_ccDealt, rA_wardskilled, rA_wardsPlaced, rA_visionWardsBought, rA_minionskilled, rA_neutralKilled, rA_firstBloodKill, rA_firstTowerAssist, rA_firstTowerKill, ChampionWinrateWeighted\n")

# skip first line of file containing the column headers
skip = next(r)

for x in range(0,500000):
	start = next(r)
	if start is None:
		# end of file was reached
		print("next line was null")
	else:
		# output list		
		outputList = []

		# rows for blue team
		blue1 = start
		blue2 = next(r)
		blue3 = next(r)
		blue4 = next(r)
		blue5 = next(r)

		# rows for red team
		red1 = next(r)
		red2 = next(r)
		red3 = next(r)
		red4 = next(r)
		red5 = next(r)
		
		# match info variables
		matchNum = blue1[0].lstrip()
		matchID = blue1[1].lstrip()
		
		outputList.append(matchNum)
		outputList.append(matchID)
		
		blueAverage = 0
		redAverage = 0
		ratio = 0
		for y in range(6,14):
		# y = 6: Champion KDA
		# y = 7: Champion Winrate
		# y = 8: Champion Games Played
		# y = 9: Champion Playrate
		# y = 10: Playrate above 10% = 1, below 10% = 0. Judges the overall experience of the team
		# y = 11: Season Games Played
		# y = 12: Season Winrate
		# y = 13: Season KDA
			blueAverage = round(((float(blue1[y]) + float(blue2[y]) + float(blue3[y]) + float(blue4[y]) + float(blue5[y]))/5), 2)
			redAverage = round(((float(red1[y]) + float(red2[y]) + float(red3[y]) + float(red4[y]) + float(red5[y]))/5), 2)
			#ratio = round(blueAverage/redAverage,3)
			difference = blueAverage - redAverage
			
			# add stat to output
			outputList.append(difference)
				
		# calculate the damage composition: Ability Power vs. Attack Power
		# a balanced damage comp. will have a score close to 25 / highest avg: 40 (all AD) / lowest avg: 10 (all AP)
		blueAverage = round(((float(blue1[15]) + float(blue2[15]) + float(blue3[15]) + float(blue4[15]) + float(blue5[15]))/5), 2)
		redAverage = round(((float(red1[15]) + float(red2[15]) + float(red3[15]) + float(red4[15]) + float(red5[15]))/5), 2)
		difference = blueAverage - redAverage
		outputList.append(difference)
		
		for z in range(17,21):
			# z = 17: recent performance: kills
			# z = 18: recent performance: assists
			# z = 19: recent performance: deaths
			# z = 20: recent performance: KDA
			blueAverage = round(((float(blue1[z]) + float(blue2[z]) + float(blue3[z]) + float(blue4[z]) + float(blue5[z]))/5), 2)
			redAverage = round(((float(red1[z]) + float(red2[z]) + float(red3[z]) + float(red4[z]) + float(red5[z]))/5), 2)
			#ratio = round(blueAverage/redAverage,3)
			difference = blueAverage - redAverage
			
			# add stat to output
			outputList.append(difference)
			
		for c in range(23,37):
			# c = 23 - recent performance: winrate
			# c = 24 - recent performance: gold per minute
			# c = 25 - recent performance: average time to win
			# c = 26 - recent performance: average damage dealt to champions
			# c = 27 - recent performance: crowd control dealt
			# c = 28 - recent performance: wards killed
			# c = 29 - recent performance: wards placed
			# c = 30 - recent performance: vision wards bought
			# c = 31 - recent performance: minions killed
			24# c = 32 - recent performance: neutral monsters killed
			# c = 33 - recent performance: first blood assists
			# c = 34 - recent performance: first blood kill 
			# c = 35 - recent performance: first tower assist 
			# c = 36 - recent performance: first tower kill
			blueAverage = round(((float(blue1[c]) + float(blue2[c]) + float(blue3[c]) + float(blue4[c]) + float(blue5[c]))/5), 2)
			redAverage = round(((float(red1[c]) + float(red2[c]) + float(red3[c]) + float(red4[c]) + float(red5[c]))/5), 2)
			difference = blueAverage - redAverage
			
			# add statistic to output
			outputList.append(difference)	
			
			
		# calculate weighted champion winrate 
		# use season winrate if they have less than 8 games played on their champion
			
		weightedBlue = 0
		weightedRed = 0
		
		# winrate = blue[7]
		# gamesplayed = blue[8]
		if float(blue1[8]) < 10:
			weightedBlue = weightedBlue + float(blue1[12])
		else:
			weightedBlue = weightedBlue + float(blue1[7])
		if float(blue2[8]) < 10:
			weightedBlue = weightedBlue + float(blue2[12])
		else:
			weightedBlue = weightedBlue + float(blue2[7])
		if float(blue3[8]) < 10:
			weightedBlue = weightedBlue + float(blue3[12])
		else:
			weightedBlue = weightedBlue + float(blue3[7])
		if float(blue4[8]) < 10:
			weightedBlue = weightedBlue + float(blue4[12])
		else:
			weightedBlue = weightedBlue + float(blue4[7])
		if float(blue5[8]) < 10:
			weightedBlue = weightedBlue + float(blue5[12])
		else:
			weightedBlue = weightedBlue + float(blue5[7])
		
		# RED TEAM
		
		if float(red1[8]) < 10:
			weightedRed = weightedRed + float(red1[12])
		else:
			weightedRed = weightedRed + float(red1[7])
		if float(red2[8]) < 10:
			weightedRed = weightedRed + float(red2[12])
		else:
			weightedRed = weightedRed + float(red2[7])
		if float(red3[8]) < 10:
			weightedRed = weightedRed + float(red3[12])
		else:
			weightedRed = weightedRed + float(red3[7])
		if float(red4[8]) < 10:
			weightedRed = weightedRed + float(red4[12])
		else:
			weightedRed = weightedRed + float(red4[7])
		if float(red5[8]) < 10:
			weightedRed = weightedRed + float(red5[12])
		else:
			weightedRed = weightedRed + float(red5[7])
		
		# compute the ratio and append to list
		higherChampionRatio = round(weightedBlue/weightedRed,3)
		outputList.append(higherChampionRatio)	
		
	
		# Print to file	
		output.write(str(outputList[0]) + ","
		+ str(outputList[1]) + ","
		+ str(outputList[2]) + ","
		+ str(outputList[3]) + ","
		+ str(outputList[4]) + ","
		+ str(outputList[5]) + ","
		+ str(outputList[6]) + ","
		+ str(outputList[7]) + ","
		+ str(outputList[8]) + ","
		+ str(outputList[9]) + ","
		+ str(outputList[10]) + ","
		+ str(outputList[11]) + ","
		+ str(outputList[12]) + ","
		+ str(outputList[13]) + ","
		+ str(outputList[14]) + ","
		+ str(outputList[15]) + ","
		+ str(outputList[16]) + ","
		+ str(outputList[17]) + ","
		+ str(outputList[18]) + ","
		+ str(outputList[19]) + ","
		+ str(outputList[20]) + ","
		+ str(outputList[21]) + ","
		+ str(outputList[22]) + ","
		+ str(outputList[23]) + ","
		+ str(outputList[24]) + ","
		+ str(outputList[26]) + ","
		+ str(outputList[27]) + ","
		+ str(outputList[28]) + ","
		+ str(outputList[29]))
		output.write("\n")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

