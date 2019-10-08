from flask import Flask
from flask import request
from surplus import *
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from sms.sms import *

app = Flask(__name__)

@app.route("/getAuctionByNumber")
def getAuctionByNumber():
    auctionNum = request.args.get('auctionNumber')
    auctionInfo = sp.auctionDict[int(auctionNum)]
    return auctionInfo.display()

@app.route("/listAllAuctions", methods=['GET', 'POST'])
def listAllAuctions():
    destinationPhoneNumber = request.args.get('destinationPhoneNumber', None)
    allAuctions = ''
    for i in sp.auctionDict.values():
        if destinationPhoneNumber is None:
            allAuctions += i.display()
        else:
            allAuctions = i.display()
            messageHandler.sendMessageNoHTTP(destinationPhoneNumber,allAuctions)
    return allAuctions

if __name__ == "__main__":
    sp=Surplus()
    sp.processAuctions()
    sp.toCSV()
    messageHandler = sms()
    app.run(debug=True)
