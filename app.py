#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "create-meeting":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    #zone = parameters.get("bank-name")
    #Title = "Hack #101"
    speech = "The of bot is in the WEBHOOK" 
    #+ str(cost[zone])
    print("Response:")
    print(speech)
    return {
        "speech": result,
        "displayText": speech,
	"platform": "google",
	"textToSpeech": "Audio response",
	"type": "simple_response"
        #"data": {},
        #"contextOut": [],
        #"source": "BankRates"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')

