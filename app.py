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
        res = json.dumps(res, indent= 4)
        print("Result:")
        print(res)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "findBranchLink":
        result = findBranchLink(req)
    if req.get("result").get("action") == "findGuide":
    	result = findGuide(req)
    else:
    	result = {}
    return result

def findBranchLink(req):
	result = req.get("result")
        print (result)
        parameters = result.get("parameters")
        print(parameters)
        branch = parameters.get("branch")
        print(branch)
        link = {'CSE': 'www.google.co.in'}
        data = json.load(open('data.json'))
        branches = data['branches']
        print (branches)
        for i in range(len(branches)):
        	if "CSE" == branches[i]['branch']:
        		index = i
        		break
        print i
        print index
        if index != -1:
        	link = data['branches'][index]['link']
        	speech = ("This branch is available. \n Read more at %s" %(link))
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                "source": "Heere"
                }

if __name__ == '__main__':
        port = int(os.getenv('PORT', 80))
        print ("Starting on port %d" % port)
        app.run(debug = False, port = port, host = '0.0.0.0')
        
        
    
'''
def comment():
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = makeYqlQuery(req)
    if yql_query is None:
        return {}
    yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    result = urlopen(yql_url).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res


def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Today the weather in " + location.get('city') + ": " + condition.get('text') + \
             ", And the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
        


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
    }'''
