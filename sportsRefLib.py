# !python3

from sportsipy.ncaab.teams import Teams
from datetime import date

today = date.today()


for team in Teams():
    print(team.name)
    schedule = team.schedule
    for game in schedule:
        print(game)
        if game.date > today - 5:
            print(game.boxscore)
            print(game.result)
            