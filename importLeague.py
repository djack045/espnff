
import csv

from espnff import League

#print(dir(League))  # Look at attributes of object
#print(type(League)) # Look at type of object

league_id = 1339984
year = 2017
league = League(league_id, year)

#print(league)

#print(league.teams)

#print(league.Matchup)

#print(league.power_rankings(week=9))
# Split up team info

teamList= league.teams
print(teamList)
print(len(teamList))

numTeams = len(teamList)
ii = 0
teamArray = []
while ii < numTeams:
	refTeam = league.teams[ii]
	print(refTeam.owner)
	teamArray.append([ii, refTeam.owner, refTeam.schedule])
	
	#print(ii, refTeam.owner, refTeam.schedule)
	#print(ii, refTeam.owner, refTeam.mov)
	ii += 1 # Add 1 to ii to continue loop

#print(teamArray)
print(type(teamArray))
#team1 = league.teams[0]
#print(team1.owner)

#print(team1.schedule)

#print(league.scoreboard())

# Write to CSV
#csvfile = "C:/Users/djack/Git/espnff/teamArray.txt"
#with open(csvfile, "w") as output:
#    writer = csv.writer(output, lineterminator='\n')
#    for val in teamArray():
#        writer.writerow([val])  

# Write List to CSV
csvfile = "C:/Users/djack/Git/espnff/teamArray.csv"
with open(csvfile, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(teamArray)
