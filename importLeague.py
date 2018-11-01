
import csv

from espnff import League
league_id = 1339984
year = 2017
league = League(league_id, year)

#print(league)

#print(league.teams)

#print(league.Matchup)

#print(league.power_rankings(week=9))
# Split up team info
team1 = league.teams[0]

print(team1.owner)

print(team1.schedule)

print(league.scoreboard())

# Write to CSV
csvfile = "C:\Users\djack\Git\espnff\scoreboard.txt"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in league.scoreboard():
        writer.writerow([val])  


