from flask import Flask
from surplus import *
app = Flask(__name__)

@app.route("/surplus")
def surplus():
    zz=Surplus()
    zz.processAuctions()
    zz.toCSV()

if __name__ == "__main__":
    app.run(debug=True)
