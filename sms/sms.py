# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route("/listAllAuctions", methods=['GET', 'POST'])
def listAllAuctionsSMS():
    resp = MessagingResponse()
    resp.message

