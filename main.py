from flask import Flask
from flask import request
from surplus import *
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from sms.sms import *

app = Flask(__name__)

'''@app.route("/surplus")
def surplus():
    zz=Surplus()
    zz.processAuctions()
    zz.toCSV()
    return zz'''

@app.route("/getAuctionByNumber")
def getAuctionByNumber():
    auctionNum = request.args.get('auctionNumber')
    auctionInfo = sp.auctionDict[int(auctionNum)]
    return auctionInfo.display()

@app.route("/listAllAuctions", methods=['GET', 'POST'])
def listAllAuctions():
    allAuctions = ''
    for i in sp.auctionDict.values():
        allAuctions += i.display()
    messageHandler.sendMessage
    return allAuctions

if __name__ == "__main__":
    sp=Surplus()
    sp.processAuctions()
    messageHandler = sms()
    app.run(debug=True)
