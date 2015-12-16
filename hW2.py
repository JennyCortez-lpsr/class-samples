print("These are my teammates from my cross country team:")

team = ['Jenny', 'Joe', 'Ally', 'Angel', 'Melissa', 'Josh']

print(team)

num = 1

team.sort()

for team_mates in team:
	team_mates = str(team_mates)
	print(str(num) + team_mates)
	num = num + 1
	

