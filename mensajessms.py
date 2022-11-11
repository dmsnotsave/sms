from twilio.rest import Client 
import time
 
account_sid = 'AC5487bfc745758cd20933162232813171' 
auth_token = 'c43db47ec0ea4f740a14b9aa402c5add' 
client = Client(account_sid, auth_token) 
 

try:
  while 1<2:
      time.sleep(60)
      print("envia")
      message = client.messages.create(
                              from_='+19789066610',
                                body='holi',      
                                to='+51951400060' 
                            ) 
      print(message.sid)
except:
  print('fallo')