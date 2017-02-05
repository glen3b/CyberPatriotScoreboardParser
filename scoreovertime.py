#!/usr/bin/python3

import sys
from lxml import html
import urllib3
import re

http = urllib3.PoolManager()

baseUrl = 'http://scoreboard.uscyberpatriot.org/'

scoresPage = html.fromstring(http.request('GET', baseUrl + 'team.php?team=' + sys.argv[1]).data)

# XPath for chart script: /html/body/div[2]/div/script[1]
chart = scoresPage.xpath('/html/body/div[2]/div/script[1]')[0]

scoreTimes = re.compile(r'\[\'([0-9]{2}/[0123456789 :]+)\'((, (-?[0-9]{1,3}|null))+)\],?', re.MULTILINE)
reSearch = scoreTimes.findall(chart.text)

for res in reSearch:
    # Tuple result
    # Capture 0 is time
    # Capture 1 is screwyformat scores
    print(res[0], end='')

    for score in filter(None, res[1].split(',')):
        print('\t' + score, end='')

    print()