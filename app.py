import urllib, json, os, sys
from flask import Flask, request, make_response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
        #Webhook verification
        return "Project verified", 200

@app.route('/webhook', methods=['GET'])
def verify():
        #Webhook verification
        return "Webhook verified", 200
        
@app.route('/webhook', methods=['POST'])
def webhook():        
        print("********")
        print("((((")
        req = request.get_json(silent=True, force=True)
        print("Request: ")
        print(json.dumps(req, indent = 4))
        res = makeWebhookResult(req)
        res = json.dumps(res, indent= 4)
        print(res)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

def makeWebhookResult(req):
        if req.get("result").get("action") != "findBranchLink":
                return()
        result = req.get("result")
        print("A1")
        parameters = result.get("parameters")
        print(parameters)
        branch = parameters.get("branch")
        print(branch)
        link = {'CSE': 'www.google.co.in'}
        speech = ("The link is " + str(link[branch]))
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                "source": "Heere"
                }

if __name__ == '__main__':
        port = int(os.getenv('PORT', 80))
        print ("Starting on port %d" %(port))
        app.run(debug = True, port = port, host='0.0.0.0')

