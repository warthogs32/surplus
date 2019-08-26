from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']
my_num = "+12153302416"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18052359605",
    from_=my_num,
    body="Hello from Python!")

print(message.sid)
