# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
class sms:
    ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN') 
    origin_number = os.getenv('ORIGIN_NUM') 
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def sendMessageHTTP(self, messageToSend):
        resp = MessagingResponse()
        resp.message(messageToSend)
        return str(resp)
    def sendMessageNoHTTP(self, destinationNumber, messageToSend):
        message = self.client.messages.create(
            body=messageToSend,
            from_= sms.origin_number,
            to = destinationNumber
        )
