
import bs4
import requests
import re

from datetime import date
from datetime import timedelta

def create_line(length):
    line = ""
    for x in range(0, length):
        line += '-'
    return line

def create_right_ending(length):
    line = ""
    for x in range(0, 43 - length):
        line += ' '
    return line + '|'

def process_date(date):
    formattedDate = date.strftime('%Y%m%d')
    url = 'https://espn.com/mens-college-basketball/schedule/_/date/' + formattedDate

    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    results = soup.select('.teams__col')

    if (date != date.today()):
        print('')
        print('Yesterday\'s Close Games')
        print(create_line(50))
    else:
        print('')
        print('Today\'s Close Games')
        print(create_line(50))

    for result in results:
        score = result.findChildren('a')[0].getText(strip = True)
        scores = score.split(',')

        score1 = re.search('\d+', scores[0]).group()
        score2 = re.search('\d+', scores[1]).group()

        scoreDiff = abs(int(score1) - int(score2))

        if scoreDiff < 8:
            fullTeamNames = result.fetchPreviousSiblings('td')
            team1 = fullTeamNames[0].getText(strip = True).replace('@', '')
            team2 = fullTeamNames[1].getText(strip = True).replace('@', '')
            print('| ' + team1 + ' vs ' + team2 + create_right_ending(len(team1) + len(team2)))
        
    print(create_line(50))

today = date.today()
yesterday = today - timedelta(days = 1)

process_date(yesterday)
process_date(today)