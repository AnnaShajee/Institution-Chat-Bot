import urllib
import json 

import os
import sys

from flask import Flask
from flask import request
from flask import make_response

#Starting the app in a global context
app = Flask(__name__)

@app.route('/', methods=['GET'])
def verifylink():
    #Link verification
    return "Project verified", 200

@app.route('/webhook', methods=['GET'])
def verifyweb():
    #Webhook verification
    return "Webhook verified", 200
        
@app.route('/webhook', methods=['POST'])
def webhook():        
    print("********")
    req = request.get_json()
    print("Request: ")
    print(json.dumps(req, indent = 4))
    res = makeWebhookResult(req)
    ret = json.dumps(res, indent= 4)
    print("Result:")
    print(res)
    print(ret)
    r = make_response(ret)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "findBranchLink":
        result = findBranchLink(req)
        print(result)
    elif req.get("result").get("action") == "findGuide":
        result = findGuide(req)
    else:
        result = {}
    print(result)
    return result

def findBranchLink(req):
    result = req.get("result")
    print (result)
    parameters = result.get("parameters")
    print(parameters)
    branch = parameters.get("branch")
    print(branch)
    data = json.load(open('data.json'))
    branches = data['branches']
    print (branches)
    for i in range(len(branches)):
        if "CSE" == branches[i]['branch']:
            index = i
            break
    print (i)
    print (index)
    if index != -1:
        link = data['branches'][index]['link']
        speech = ("This branch is available. Read more at %s" %(link))
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "Heere",
        "messages": [
        {
        "buttons": [
        {
        "openUrlAction": {
        "url": "https://linkUrl.com"
        },
        "title": "AoG Card Link title"
        }
        ],
        "formattedText": "AoG Card Description",
        "image": {
        "url": "http://imageUrl.com"
        },
        "platform": "google",
        "subtitle": "AoG Card Subtitle",
        "title": "AoG Card Title",
        "type": "basic_card"
        }
        ] 
        }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    print ("Starting on port %d" % port)
    app.run(debug = False, port = port, host = '0.0.0.0')
