

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json 
x='{"id": 2, "pin":"1234", "info": {"name": "John", "surname": "Smith"}, "age": 25}'
y=json.loads(x)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == ("{} {} pin:{}".format(y["info"]["name"],y["info"]["surname"],y["pin"])) :
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")
    elif body == 'specific':
        resp.message("Success")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
























