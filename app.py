import urllib
import json 

import os
import sys

from flask import Flask
from flask import request
from flask import make_response

import actions

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
    action = req.get("result").get("action")
    if action == "findBranchLink":
        print("A")
        result = findBranchLink(req)
        print(result)
    elif action == "findGuide":
        result = findGuide(req)
    elif action == "findSyllabus":
        result = findSyllabus(req)
    elif action == "contactOffice":
        result = contactOffice(req)
    elif action == "admissionQuery":
        result = admissionQuery(req)
    else:
        result = default()
    print(result)
    return result

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    print ("Starting on port %d" % port)
    app.run(debug = False, port = port, host = '0.0.0.0')
