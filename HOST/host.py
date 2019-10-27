# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import serial
account_sid = 'ACf627d2336806adfa6b0475e9739babaf'
auth_token = '1abf3c0296584cc5f7114359313f048f'
client = Client(account_sid, auth_token)
def call():
    call = client.calls.create(
                            url='http://vps736330.ovh.net:8000/resp.xml',
                            to='+447342178041',
                            from_='+447723569692'
                        )

    print(call.sid)

    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        to='+447934359814',
                        from_='+447723569692'
                    )

    print(message.sid)

with serial.Serial('/dev/ttyACM0',115200,timeout=1) as ser:
    line=ser.readline()

    if line=="help":
        call()