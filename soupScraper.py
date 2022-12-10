
import bs4
import requests

from datetime import date
from datetime import timedelta

def process_date(date):
    formattedDate = date.strftime('%Y%m%d')
    url = 'https://espn.com/mens-college-basketball/schedule/_/date/' + formattedDate

    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    results = soup.select('.teams__col')

    if (date != date.today()):
        print('Close Games Yesterday')
        print('---------------------------')
    else:
        print('Close Games Today')
        print('---------------------------')

    for result in results:
        score = result.findChildren('a')[0].getText(strip = True)
        scores = score.split(',')
        team1AndScore = scores[0].split()
        team2AndScore = scores[1].split()

        team1 = team1AndScore[0]
        team2 = team2AndScore[0]

        score1 = team1AndScore[1]
        score2 = team2AndScore[1]

        scoreDiff = abs(int(score1) - int(score2))

        if scoreDiff < 8:
            fullTeamNames = result.fetchPreviousSiblings('td')
            team1 = fullTeamNames[0].getText(strip = True).replace('@', '')
            team2 = fullTeamNames[1].getText(strip = True).replace('@', '')
            print('| ' + team1 + ' vs ' + team2 + ' |')
            print('------------------------')

today = date.today()
yesterday = today - timedelta(days = 1)

process_date(today)
process_date(yesterday)