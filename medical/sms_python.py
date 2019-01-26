import time 
from time import sleep 
from sinchsms import SinchSMS 
  
# function for sending SMS 
def sendSMS(): 
  
    # enter all the details 
    # get app_key and app_secret by registering 
    # a app on sinchSMS 
    number = '9404152440'
    app_key = '0a9f97ef1efc416094bd7cca5de5b539'
    app_secret = '78885cf86a7a44dca549b49532205def'
  
    # enter the message to be sent 
    message = 'Hello Message!!!'
  
    client = SinchSMS(app_key, app_secret) 
    print("Sending '%s' to %s" % (message, number)) 
  
    response = client.send_message(number, message) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
  
    # keep trying unless the status retured is Successful 
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id) 
  
    print(response['status']) 
  
if __name__ == "__main__": 
    sendSMS()