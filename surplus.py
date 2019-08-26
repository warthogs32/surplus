import pandas as pd
from Auction import *
from decimal import Decimal
import requests
from bs4 import BeautifulSoup
import numpy as np
import urllib.request

def load(url):
    src = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(src, "html.parser")
    return bs

allAuctions = load('https://www.publicsurplus.com/sms/calpoly,ca/list/current?orgid=3013').findAll('tr')

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
