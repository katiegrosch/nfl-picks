# for each week
	# 	for each game
	# 		take max of team 1 and team 2 value
	# 		add to array
# sort array
# print winner and chance

from bs4 import BeautifulSoup
#import requests

#url = 'https://projects.fivethirtyeight.com/2017-nfl-predictions/games/'
#r = requests.get(url)
# soup = BeautifulSoup(r.content)

soup = BeautifulSoup(open("538_11_8.html"), 'lxml')

weeks = soup.findAll('section', {"class":"week"})

for week in weeks:
	print ('\n')
	print (week.h3.string)
	picks = []
	games = week.findAll('table', {"class":"game-body"})
	for game in games:
		team0 = game.tbody.contents[0].contents[1].string
		team1 = game.tbody.contents[1].contents[1].string
		if ((game.tbody.contents[0].contents[2].string == ' ') or (game.tbody.contents[0].contents[2].string == ' PK')):
			spread0 = 0
		else:
			spread0 = float(game.tbody.contents[0].contents[2].string)
		if ((game.tbody.contents[1].contents[2].string == ' ') or (game.tbody.contents[1].contents[2].string == ' PK')):
			spread1 = 0
		else: 
			spread1 = float(game.tbody.contents[1].contents[2].string)

		#print(team0, spread0, team1, spread1)
		if (spread1 - spread0) > 0:
			pair = (team0.string, game.tbody.contents[0].contents[3].string)
			picks.append(pair)
			#print(pair)
		else:
			pair = (team1.string, game.tbody.contents[1].contents[3].string)
			picks.append(pair)
			#print(pair)

	picks.sort(key=lambda x: x[1])
	for pick in picks:
		print (pick)