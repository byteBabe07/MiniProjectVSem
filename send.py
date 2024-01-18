from twilio.rest import Client

account_sid = 'AC852a0f5c8aeae6fbf03f7f8d5bf53133'
auth_token = 'cefd8d5b15ba15024b0e8b287dab4862'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14846015240',
  body='INTRUDER ALERT!! Strange Activity Detected. Please Check',
  to='+917017322456'
)

print(message.sid)