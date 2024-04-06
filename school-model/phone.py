from twilio.rest import Client

def call():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to="",
        from_=""
    )

    print(call.sid)