# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import json
import os.path
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
class sms:
    with open(os.path.dirname(__file__) + '/../config.json') as config_file:
        appConfig = json.load(config_file)
        ACCOUNT_SID = appConfig["TWILIO"]["ACCOUNT_SID"]
        AUTH_TOKEN = appConfig["TWILIO"]["AUTH_TOKEN"]
        origin_number = appConfig["TWILIO"]["ORIGIN_NUMBER"]
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def sendMessageHTTP(self, messageToSend):
        resp = MessagingResponse()
        resp.message(messageToSend)
        return str(resp)
    def sendMessageNoHTTP(self, destinationNumber, messageToSend):
        message = self.client.messages.create(
            body = messageToSend,
            from_= sms.origin_number,
            to = destinationNumber
        )
