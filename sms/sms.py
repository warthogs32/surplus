# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
class sms:
    account_sid = "ACf6519377bf2ea71fdfb027a4ac774240"
    auth_token = "3ed7b245fe962eef8e137dc47c90755e"
    client = Client(account_sid, auth_token)

    def sendMessage(self, messageToSend):
        resp = MessagingResponse()
        resp.message(messageToSend)
        return str(resp)

