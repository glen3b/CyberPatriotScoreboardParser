#!/usr/bin/python3
import sys
from lxml import html
import urllib3

http = urllib3.PoolManager()

baseUrl = 'http://scoreboard.uscyberpatriot.org/'

teamsPage = http.request('GET', baseUrl + 'index.php?division=Open&tier=Platinum')
teamsPageData = html.fromstring(teamsPage.data)
teamsTable = teamsPageData.xpath('/html/body/div[2]/div/table')[0]

# Root page XPath for teams table:
# /html/body/div[2]/div/table/tbody

#for team in teamsTable:
#    print(html.tostring(team))

# Score page XPath for scores table:
# /html/body/div[2]/div/table[2]/tbody

printOverall = '-a' in sys.argv

def stripColText(col):
    if col.text != None:
        return col.text.strip()
    else:
        return ''

def printScores(team):
    scoresPage = html.fromstring(http.request('GET', baseUrl + team).data)
    scoresTable = scoresPage.xpath('/html/body/div[2]/div/table[2]')[0]
    #print(html.tostring(scoresTable))
    for row in scoresTable:
        if row[0].text == 'Team':
            continue

        for col in row:
            if col.text != None:
                print(col.text.strip(), end='\t')

        print()

#print('Team\tImage\t\t\t\t\tTime\tFixed\tRemaining\tPenalties\tScore\tWarnings')

for team in teamsTable:
    if 'href' in team.attrib:
        # ignore teams who aren't really teams
        if team[0].text == 'Team Number':
            continue

        #print(team.attrib['href'])
        if printOverall:
            print(stripColText(team[0]) + '\t' + stripColText(team[5]) + '\t' + stripColText(team[6]))
        else:
            printScores(team.attrib['href'])
