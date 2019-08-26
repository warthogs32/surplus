from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf6519377bf2ea71fdfb027a4ac774240"
# Your Auth Token from twilio.com/console
auth_token  = "3ed7b245fe962eef8e137dc47c90755e"
my_num = "+12153302416"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18052359605",
    from_=my_num,
    body="Hello from Python!")

print(message.sid)
