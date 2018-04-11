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
    print(ret)
    r = make_response(ret)
    r.headers['Content-Type'] = 'application/json'
    return r
  
def makeWebhookResult(req):
    action = req.get("result").get("action")
    print(action)
    if action == "findBranchLink":
        result = findBranchLink(req)
    elif action == "findGuide":
        result = findGuide(req)
    elif action == "findDean":
        result = findDean(req)
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
            "image": {
            "url": "http://vit.ac.in/images/placements/placement2.JPG",
            "accessibilityText": "Branches Offered"
            },
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
            "image": {
            "url": "http://vit.ac.in/images/placements/placement2.JPG",
            "accessibilityText": "Branches Offered"
            },
            "formattedText": speech1,
            "platform": "google",
            "title": "Course not offered",
            "type": "basic_card"
            }
            ] 
            }

def findSyllabus(req):
    print("C")
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
        link = data['branches'][index]['syllabus']
        name = data['branches'][index]['name']
        speech1 = ("The syllabus for %s " %(name))
        speech2 = ("is available at %s. " %(link))
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
            "title": "Find syllabus here."
            }
            ],
            "image": {
            "url": "http://vit.ac.in/images/placements/placement2.JPG",
            "accessibilityText": "Branches Offered"
            },
            "formattedText": speech1,
            "platform": "google",
            "subtitle": "Syllabus",
            "title": name,
            "type": "basic_card"
            }
            ] 
            }
    else: 
        speech1 = ("I'm sorry, we don't offer that course at VIT, Vellore. ")
        link = "http://vit.ac.in/admissions/ug"
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
            "image": {
            "url": "http://vit.ac.in/images/placements/placement1.JPG",
            "accessibilityText": "Branches Offered"
            },
            "formattedText": speech1,
            "platform": "google",
            "title": "Course not offered",
            "type": "basic_card"
            }
            ] 
            }

def findDean(req): 
    print("D")
    result = req.get("result")
    print (result)
    parameters = result.get("parameters")
    print(parameters)
    p_school = parameters.get("school")
    print(p_school)
    data = json.load(open('data.json'))
    deans = data['organization']['dean']
    print (deans)
    flag = "false"
    if deans.get(p_school) is not None:
        flag = "true"
    print(flag)
    if flag == "true":
        school = data['organization']['dean'][p_school]['school']
        name = data['organization']['dean'][p_school]['name']
        link = data['organization']['dean'][p_school]['link']
        image = data['organization']['dean'][p_school]['image']
        speech1 = ("The Dean of %s is %s. " %(school, name))
        speech2 = ("Find all the faculty at %s. " %(link))
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
            "title": "Find all the faculty here."
            }
            ],
            "image": {
            "url": image,
            "accessibilityText": "Dean of %s" %(school)
            },
            "formattedText": speech1,
            "platform": "google",
            "subtitle": "Dean, %s" %(school),
            "title": name,
            "type": "basic_card"
            }
            ] 
            }
    else: 
        speech1 = ("I'm sorry, that doesn't associate to a school at VIT, Vellore. ")
        link = "http://vit.ac.in/academics/schools"
        speech2 = ("Find our schools at %s" %(link))
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
            "title": "Find our schools here."
            }
            ],
            "image": {
            "url": "http://vit.ac.in/images/schools/vitschoolimage.jpg",
            "accessibilityText": "Schools at VIT"
            },
            "formattedText": speech1,
            "platform": "google",
            "title": "School not found",
            "type": "basic_card"
            }
            ] 
            }

def findGuide(req): 
    print("E")
    result = req.get("result")
    print (result)
    parameters = result.get("parameters")
    print(parameters)
    interest = parameters.get("specialization")
    print(interest)
    data = json.load(open('data.json'))
    faculty = data['faculty']
    print (faculty)
    flag = "false"
    for index in range(len(faculty)):
        area = faculty[index]['areas']
        for num in range(len(area)):
            if area[num] == interest:
                flag = "true"
                break
    print(flag)
    if flag == "true":
        school = data['faculty'][index]['school']
        name = data['faculty'][index]['name']
        link = data['faculty'][index]['link']
        image = data['faculty'][index]['image']
        role = data['faculty'][index]['role']
        speech1 = ("%s, %s at %s, has expertise in %s. " %(name, role, school, interest))
        speech2 = ("Find %s at %s. " %(name, link))
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
            "title": "Find %s here." %(name)
            }
            ],
            "image": {
            "url": image,
            "accessibilityText": "%s" %(name)
            },
            "formattedText": speech1,
            "platform": "google",
            "subtitle": "%s, %s" %(role, school),
            "title": name,
            "type": "basic_card"
            }
            ] 
            }
    else: 
        speech1 = ("I'm sorry, none of our faculties seem to be researching in %s. Try another interest for a guide." %(interest))
        link = "http://vit.ac.in/academics/schools"
        speech2 = ("Find our schools at %s" %(link))
        speech = speech1 + speech2
        print(speech)
        return {
            "speech": speech,
            "displayText": speech,
            "source": "Institution-Chat-Bot"
            }

def contactOffice(req): 
    print("D")
    result = req.get("result")
    print (result)
    parameters = result.get("parameters")
    print(parameters)
    p_school = parameters.get("school")
    print(p_school)
    data = json.load(open('data.json'))
    deans = data['organization']['dean']
    print (deans)
    flag = "false"
    if deans.get(p_school) is not None:
        flag = "true"
    print(flag)
    if flag == "true":
        school = data['organization']['dean'][p_school]['school']
        name = data['organization']['dean'][p_school]['name']
        link = data['organization']['dean'][p_school]['link']
        image = data['organization']['dean'][p_school]['image']
        speech1 = ("The Dean of %s is %s. " %(school, name))
        speech2 = ("Find all the faculty at %s. " %(link))
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
            "title": "Find all the faculty here."
            }
            ],
            "image": {
            "url": image,
            "accessibilityText": "Dean of %s" %(school)
            },
            "formattedText": speech1,
            "platform": "google",
            "subtitle": "Dean, %s" %(school),
            "title": name,
            "type": "basic_card"
            }
            ] 
            }
    else: 
        speech1 = ("I'm sorry, that doesn't associate to a school at VIT, Vellore. ")
        link = "http://vit.ac.in/academics/schools"
        speech2 = ("Find our schools at %s" %(link))
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
            "title": "Find our schools here."
            }
            ],
            "image": {
            "url": "http://vit.ac.in/images/schools/vitschoolimage.jpg",
            "accessibilityText": "Schools at VIT"
            },
            "formattedText": speech1,
            "platform": "google",
            "title": "School not found",
            "type": "basic_card"
            }
            ] 
            }

def admissionQuery(req): 
    print("D")
    result = req.get("result")
    print (result)
    parameters = result.get("parameters")
    print(parameters)
    p_school = parameters.get("school")
    print(p_school)
    data = json.load(open('data.json'))
    deans = data['organization']['dean']
    print (deans)
    flag = "false"
    if deans.get(p_school) is not None:
        flag = "true"
    print(flag)
    if flag == "true":
        school = data['organization']['dean'][p_school]['school']
        name = data['organization']['dean'][p_school]['name']
        link = data['organization']['dean'][p_school]['link']
        image = data['organization']['dean'][p_school]['image']
        speech1 = ("The Dean of %s is %s. " %(school, name))
        speech2 = ("Find all the faculty at %s. " %(link))
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
            "title": "Find all the faculty here."
            }
            ],
            "image": {
            "url": image,
            "accessibilityText": "Dean of %s" %(school)
            },
            "formattedText": speech1,
            "platform": "google",
            "subtitle": "Dean, %s" %(school),
            "title": name,
            "type": "basic_card"
            }
            ] 
            }
    else: 
        speech1 = ("I'm sorry, that doesn't associate to a school at VIT, Vellore. ")
        link = "http://vit.ac.in/academics/schools"
        speech2 = ("Find our schools at %s" %(link))
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
            "title": "Find our schools here."
            }
            ],
            "image": {
            "url": "http://vit.ac.in/images/schools/vitschoolimage.jpg",
            "accessibilityText": "Schools at VIT"
            },
            "formattedText": speech1,
            "platform": "google",
            "title": "School not found",
            "type": "basic_card"
            }
            ] 
            }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    print ("Starting on port %d" % port)
    app.run(debug = False, port = port, host = '0.0.0.0')
