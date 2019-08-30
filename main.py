from flask import Flask
from flask import request
from surplus import *
app = Flask(__name__)

@app.route("/surplus")
def surplus():
    zz=Surplus()
    zz.processAuctions()
    zz.toCSV()
    return zz
    '''disp = ''
    for i in zz.auctionList:
        disp += i.display()
    return disp'''

@app.route("/getAuctionByNumber")
def getAuctionByNumber():
    surp = surplus()
    auctionNum = request.args.get('auctionNumber')
    auctionInfo = surp.auctionDict[int(auctionNum)]
    auctionInfoString = ''
    for i in auctionInfo:
        auctionInfoString += str(i) + "\n"
    return auctionInfoString
    


if __name__ == "__main__":
    app.run(debug=True)
