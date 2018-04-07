import urllib, json,os, sys
from flask import Flask, request, make_response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
        #Webhook verification
        return "Project verified", 200

headers = {
        'Authorization': 'Bearer 28c2863125f64b9c8835c5d6c3b7aea1',
        }
response = requests.get('https://dialogflow.com/v1/query?v=20170712&e=Welcome&timezone=Asia/Calcutta&lang=en&sessionId=123456', headers=headers)

params = (
        ('v', '20170712'),
        ('e', 'Welcome'),
        ('lang', 'en'),
        ('sessionId', 'fd11cd55-0dc0-4ba8-9404-a69f82a6e639'),
        ('timezone', 'Asia/Calcutta'),
        )
        
@app.route('/', methods=['POST'])
def webhook():
        
        print("********")
        print("((((")
        req = request.get_json()
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
        app.run(debug = True, port = port)

