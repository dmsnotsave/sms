from twilio.rest import Client
import time
import requests

account_sid = 'AC5487bfc745758cd20933162232813171'

auth_token = "3f3d93db6cfd977e7a994fafbd4e9d5b"

client = Client(account_sid, auth_token)


urlll = 'https://libre-api-4bfd9-default-rtdb.firebaseio.com/api/llamadas.json'

ax = requests.get(urlll)
jsooon = ax.json()
timeee = jsooon['timee']
try:
    while 1<2:
        print('Inició')
        time.sleep(timeee)
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to="+51951400060",
            from_="+19789066610")
        print(call.sid)
except:
    print('error')