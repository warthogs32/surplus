from flask import Flask
from Surplus import *
app = Flask(__name__)

@app.route("/sms")
def hello():
    zz=Surplus();
    return zz.toCSV()

if __name__ == "__main__":
    app.run(debug=True)
