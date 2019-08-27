import pandas as pd
import csv
from Auction import *
from Time import *
from decimal import Decimal
import requests
from bs4 import BeautifulSoup
import numpy as np
import urllib.request

auctionList = []
auctionDict = {}

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def loadSrc(url):
    src = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(src, "html.parser")
    return bs

def parseTime(timeString):
    timeStringList = list(timeString.split(" "))
    splitTime =[]
    lst=[]
    timelist=[0] * 6
    for i in timeStringList:
        lst.append(i)
        if(not isInt(i)):
            splitTime.append(lst)
            lst = []
    for j in splitTime:
        if j[1] == 'months':
            timelist[0] = j[0]
        if j[1] == 'weeks':
            timelist[1] = j[0]
        if j[1] == 'days':
            timelist[2] = j[0]
        if j[1] == 'hours':
            timelist[3] = j[0]
        if j[1] == 'min':
            timelist[4] = j[0]
        if j[1] == 'seconds':
            timelist[5] = j[0]
    return Time(timelist[0], timelist[1], timelist[2], timelist[3], timelist[4], timelist[5])

allAuctions = loadSrc('https://www.publicsurplus.com/sms/ucberkeley,ca/list/current?orgid=18446').findAll('tr')

for auctionRecord in allAuctions:
    auctionInfo = [i for i in [td.get_text().strip() for td in auctionRecord.findAll('td') if td] if i]
    for item in auctionInfo:
        if len(auctionInfo) == 4:
            auctionInfo[0] = int(auctionInfo[0])
            auctionInfo[3] = auctionInfo[3].strip('$')
            time = parseTime(auctionInfo[2])
            if "," in auctionInfo[3]:
                auctionInfo[3] = auctionInfo[3].replace(",", "")
            auctionList.append(Auction(auctionInfo[0], auctionInfo[1], time, auctionInfo[3]))
            auctionDict[auctionInfo[0]] = [auctionInfo[1], time.toSeconds(), float(auctionInfo[3])]

def toCSV():
    with open('auctions.csv', mode='w') as auctions:
        csvwriter = csv.writer(auctions, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(["Auction Number", "Title", "Time Remaining", "Current Price"])
        for key, val in auctionDict.items():
            csvwriter.writerow([key, val[0], val[1], val[2]])

for i in auctionList:
    print(i.display())

print(auctionDict)
toCSV()