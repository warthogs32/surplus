import pandas as pd
import csv
import os
import json
import sys
from Models.Auction import *
from Models.Time import *
from decimal import Decimal
import pyodbc
import requests
from bs4 import BeautifulSoup
import numpy as np
import urllib.request

class Surplus(object):

    _instance = None
    auctionList = []
    auctionDict = {}
    URL = 'https://www.publicsurplus.com/sms/calpoly,ca/list/current?orgid=3013'
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Surplus, cls).__new__(cls)
        return cls._instance

    def isInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def loadSrc(self, url):
        src = urllib.request.urlopen(url).read()
        bs = BeautifulSoup(src, "html.parser")
        return bs

    def parseTime(self, timeString):
        timeStringList = list(timeString.split(" "))
        splitTime =[]
        lst=[]
        timelist=[0] * 4
        for i in timeStringList:
            lst.append(i)
            if(not self.isInt(i)):
                splitTime.append(lst)
                lst = []
        for j in splitTime:
            if j[1] == 'days':
                timelist[0] = j[0]
            if j[1] == 'hours':
                timelist[1] = j[0]
            if j[1] == 'min':
                timelist[2] = j[0]
            if j[1] == 'seconds':
                timelist[3] = j[0]
        return Time(timelist[0], timelist[1], timelist[2], timelist[3])

    def toCSV(self):
        if not os.path.exists('out'):
            os.makedirs('out')
        with open(os.path.join(os.getcwd(), 'out', 'auctions.csv'), mode='w+') as auctions:
            csvwriter = csv.writer(auctions, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(["Auction Number", "Title", "Time Remaining", "Current Price"])
            for key, val in self.auctionDict.items():
                csvwriter.writerow([key, val.auctionTitle, val.auctionTime.toEndDateStamp(), val.auctionCurrentPrice])

    def processAuctions(self):
        allAuctions = self.loadSrc(self.URL).findAll('tr')
        for auctionRecord in allAuctions:
            auctionInfo = [i for i in [td.get_text().strip() for td in auctionRecord.findAll('td') if td] if i]
            if(len(auctionInfo) == 4):
                auctionInfo[0] = int(auctionInfo[0])
                auctionInfo[3] = auctionInfo[3].strip('$')
                time = self.parseTime(auctionInfo[2])
                if "," in auctionInfo[3]:
                    auctionInfo[3] = auctionInfo[3].replace(",", "")
                currentAuction = Auction(auctionInfo[0], auctionInfo[1], time, auctionInfo[3])
                self.auctionList.append(currentAuction)
                self.auctionDict[auctionInfo[0]] = currentAuction
    def writeToSQL(self):
        with open('db.json') as json_file:
            db_info = json.load(json_file)
            conn = pyodbc.connect('DRIVER='+db_info['drvr']+';SERVER='+db_info["server"]+';DATABASE='+db_info["database"]+';UID='+db_info["user"]+';PWD='+db_info["password"])
            cursor = conn.cursor()
