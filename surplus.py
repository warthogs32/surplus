import pandas as pd
from decimal import Decimal
import requests
from bs4 import BeautifulSoup
import numpy as np
import urllib.request

class Auction:
    def __init__(self, number, title, time, cp):
        self.auctionNum=number
        self.auctionTitle=title
        self.auctionTime=time
        self.auctionCurrentPrice=float(cp)
    def display(self):
        return ("Auction Number: {} \nTitle: {} \nTime Remaining: {} \nCurrent Price: ${} \n".format(self.auctionNum, self.auctionTitle, self.auctionTime, self.auctionCurrentPrice))

url = 'https://www.publicsurplus.com/sms/calpoly,ca/list/current?orgid=3013'
page = urllib.request.urlopen(url)
src = page.read()
page.close()
bs = BeautifulSoup(src, "html.parser")

allAuctions = bs.findAll('tr')

auctionList = []

for auctionRecord in allAuctions:
    auctionInfo = [i for i in [td.get_text().strip() for td in auctionRecord.findAll('td') if td] if i]
    for item in auctionInfo:
        if len(auctionInfo) == 4:
            auctionInfo[0] = int(auctionInfo[0])
            auctionInfo[3] = auctionInfo[3].strip('$')
            auctionList.append(Auction(auctionInfo[0], auctionInfo[1], auctionInfo[2], auctionInfo[3]))

for i in auctionList:
    print(i.display())
