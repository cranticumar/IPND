from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc50ee28984bee4c8057391804b58f254"
auth_token  = "0b9542ef5036662d5f3f1d914a6d13a5"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Niha, I love you <3",
    to="+919618253216",    # Replace with your phone number
    from_="+12056248837") # Replace with your Twilio number
print message.sid