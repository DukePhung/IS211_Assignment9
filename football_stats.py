#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
"""Parsing football stats."""

from bs4 import BeautifulSoup
import csv
import urllib.request, urllib.parse, urllib.error

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns"
player_list = []

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

trs = soup.find_all('tr')
for tr in trs:
    # f.writerow(tr)
    tds = tr.find_all('td')
    
    try:
        names = str(tds[0].get_text())
        position = str(tds[1].get_text())
        team = str(tds[2].get_text())
        games = str(tds[3].get_text())
        points = str(tds[4].get_text())
        pts_per_game = str(tds[5].get_text())
        touchdown = str(tds[6].get_text())
    except:
        continue

    player_list.append([names, position, team, touchdown])

for n in range(20):
    print(player_list[n])
    
