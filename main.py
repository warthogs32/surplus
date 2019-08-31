from flask import Flask
from flask import request
from surplus import *
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

'''@app.route("/surplus")
def surplus():
    zz=Surplus()
    zz.processAuctions()
    zz.toCSV()
    return zz'''

@app.route("/getAuctionByNumber")
def getAuctionByNumber():
    surp = Surplus()
    auctionNum = request.args.get('auctionNumber')
    auctionInfo = surp.auctionDict[int(auctionNum)]
    return auctionInfo.display()

if __name__ == "__main__":
    zz=Surplus()
    zz.processAuctions()
    app.run(debug=True)
