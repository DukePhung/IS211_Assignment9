#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
"""Parsing AAPL stock values."""

from bs4 import BeautifulSoup
import csv
import urllib.request, urllib.parse, urllib.error

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html)

#f = csv.writer(open('apple_stock.csv', 'w'))

trs = soup.find_all('tr')

print('Closing Date\tClosing Price')

for tr in trs:
    # f.writerow(tr)
    tds = tr.find_all('td')

    try:
        date = str(tds[0].get_text())
        open_price = str(tds[1].get_text())
        high = str(tds[2].get_text())
        low = str(tds[3].get_text())
        closing = str(tds[4].get_text())
        adjusted_close = str(tds[5].get_text())
        volume = str(tds[6].get_text())
        
    except:
        continue
    
    print(date, '\t', closing)
