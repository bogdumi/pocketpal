# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import serial
import time
account_sid = 'ACf627d2336806adfa6b0475e9739babaf'
auth_token = '1abf3c0296584cc5f7114359313f048f'
client = Client(account_sid, auth_token)
def call():
    call = client.calls.create(
                            method='GET',
                            url='https://00e9e64bacaf9dbeb75b459d8a60b4418ea1efb3ee985e5357-apidata.googleusercontent.com/download/storage/v1/b/twilio69/o/resp.xml?qk=AD5uMEssDLyA_0yRelWvMAUaBGVCgDjGdI_827Y-2vS6P4mVj1oIDNEIvyWSi-MNyj-pRrSEe-8g73wBdqn2acoyJVyDQo5AKf1jtwmjMHd_iJQxYC7SN8xaONd9ppaUrmN9-wobj9YxtN4GVz6b8Gd4KBZBmX89vw6Hx9_OzjtuQOd_6_NZpX6O1ry5hVr4Cz2OJnZ3tPLRZFBMy0u07W-7P3SQTOKymGb5Q3OMzqCW8up1eVLUS2jEBHmodLypj7wBO4pYKRSAjLueWfm-zVLC3it5SAibahiIXy6wm6o9VPpZqpEAz0rYlynKSjqZxlaaOBpb2ZHy9NeLy-c6L3-PVq_9c5f-9YAwrygaU4TG0MgvwuqRCb6zw83SFFUT7EFPsBvbWVs-1AbkuQ5OnB58yWidzV2NFP_RUn-ThpGBOJTRawSBb1r1t_se3G-wK5z06ewLjqJkyPc5uqh0560Dk170m_xk6Ag_l3EqxCUczG18t9_pu_Qt7RlWpqC8S8Ri-pcRc8yUKQU9L1zz_vgA-GBFfHr-3uXIEQe0oHMDI4M8frn8o9eLfqcYAtrINWAlY8NZOds0icB3ExJsQF8CZS40I6TjlknJREVJ9ZvG_S1knFcK80PgQ2a8jk0lctgfzTKMmVnVCvBxBcX5qjKQEoQdMipLDEI6259_4DnK6_eMrn_PNQXlG78jq32suDzfIKerLddFSlK6A1gPqcIMpMzUWMenaU6kD7bOKEa_2VrEiH-iiBETrUbfXeFGt6IUL2bS4lLEgELf4xDoIAyoCol_I4nRTQ',
                            to='+447342178041',
                            from_='+447723569692'
                        )

    print(call.sid)

    message = client.messages \
                    .create(
                        body="I've fallen. Pls help.",
                        to='+447934359814',
                        from_='+447723569692'
                    )

    print(message.sid)
while True:
    with serial.Serial('/dev/ttyACM0',115200,timeout=1) as ser:
        line=ser.readline()
        print(line)
        if 'help' in str(line):
            print("HELP!")
            call()
            time.sleep(10)