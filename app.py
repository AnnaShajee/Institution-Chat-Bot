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

def findBranchLink(req):
    print("B")
    result = req.get("result")
    print (result)
    parameters = result.get("parameters")
    print(parameters)
    branch = parameters.get("branch")
    print(branch)
    data = json.load(open('data.json'))
    branches = data['branches']
    print (branches)
    flag = "false"
    for index in range(len(branches)):
        if branch == branches[index]['branch']:
            flag = "true"
            break
    print (index)
    print(flag)
    if flag == "true":
        link = data['branches'][index]['link']
        name = data['branches'][index]['name']
        school = data['branches'][index]['school']
        speech1 = ("%s is available, under %s. " %(name, school))
        speech2 = ("Read more at %s" % (link))
        speech = speech1 + speech2
        print (speech)
        return {
            "speech": speech,
            "displayText": speech,
            "source": "Institution-Chat-Bot",
            "messages": [
            {
            "displayText": speech,
            "platform": "google",
            "textToSpeech": speech,
            "type": "simple_response"
            },
            {
            "buttons": [
            {
            "openUrlAction": {
            "url": link
            },
            "title": "Read more here."
            }
            ],
            "formattedText": speech1,
            "platform": "google",
            "subtitle": school,
            "title": name,
            "type": "basic_card"
            }
            ] 
            }
    else: 
        speech1 = ("I'm sorry, we don't offer that course at VIT, Vellore. ")
        link = "http://vit.ac.in/admissions/ug."
        speech2 = ("Check out the courses offered at %s" %(link))
        speech = speech1 + speech2
        print(speech)
        return {
            "speech": speech,
            "displayText": speech,
            "source": "Institution-Chat-Bot",
            "messages": [
            {
            "displayText": speech,
            "platform": "google",
            "textToSpeech": speech,
            "type": "simple_response"
            },
            {
            "buttons": [
            {
            "openUrlAction": {
            "url": link
            },
            "title": "Find offered courses here."
            }
            ],
            "formattedText": speech1,
            "platform": "google",
            "title": "Course not offered",
            "type": "basic_card"
            }
            ] 
            }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    print ("Starting on port %d" % port)
    app.run(debug = False, port = port, host = '0.0.0.0')
