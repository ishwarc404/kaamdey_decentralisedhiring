from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

import possible_incomming
import functions

app = Flask(__name__)

user_state = {}
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()

    print(request.values)
    user_number = request.values.get('From')[9:] #will be used to store the user state


    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    print("Beginning: ",user_state)
    #need to create a filter here
    if user_number not in user_state:
        #registering the new user into the state management
        user_state[user_number] = "initial" 

    #reset
    if(incoming_msg == "reset"):
        user_state[user_number] = "initial"
        response_body = functions.initial_state()
        msg.body(response_body)
        return str(resp)



    #state 1 - initial
    if(user_state[user_number] == "initial" and incoming_msg not in ["1","2"]):
        response_body = functions.initial_state()
        msg.body(response_body)
        responded = True
    
    elif(user_state[user_number] == "initial" and incoming_msg=="1"):
        msg.body("")
        response_body = functions.switchtosearch_state()
        msg.body(response_body)
        responded = True
        user_state[user_number] = "search"
    
    elif(user_state[user_number] == "initial" and incoming_msg=="2"):
        msg.body("")
        response_body = functions.switchtosponsor_state()
        msg.body(response_body)
        responded = True
        user_state[user_number] ="sponsor"


    #state2 - searching


    #state3  - sponsor
    elif(user_state[user_number] == "sponsor"):
        msg.body("")
        response_body = functions.sponsor_name(name=incoming_msg)
        msg.body(response_body)
        responded = True
        user_state[user_number] = "sponsor_address"
    
    elif(user_state[user_number] == "sponsor_address"):
        msg.body("")
        response_body = functions.sponsor_address(address=incoming_msg)
        msg.body(response_body)
        responded = True
        user_state[user_number] = "sponsor_individualname"
    
    elif(user_state[user_number] == "sponsor_individualname"):
        msg.body("")
        response_body = functions.sponsor_individualname(individualname=incoming_msg)
        msg.body(response_body)
        responded = True
        user_state[user_number] = "sponsor_individualnumber"
    
    elif(user_state[user_number] == "sponsor_individualnumber"):
        msg.body("")
        response_body = functions.sponsor_individualnumber(individualnumber=incoming_msg)
        msg.body(response_body)
        responded = True
        user_state[user_number] = "sponsor_individualpicture"

    elif(user_state[user_number] == "sponsor_individualpicture"):
        msg.body("")
        response_body = functions.sponsor_individualpicture(individualpicture=request.values.get('MediaUrl0'))
        msg.body(response_body)
        responded = True
        user_state[user_number] = "initial"
        
  

    if not responded:
        response_body = functions.initial_state()
        msg.body("We did not understand you :( \n" + response_body)

    print("Ending: ",user_state)
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)




