import urllib, json, os, sys
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
        #Webhook verification
        return "Project verified", 200

@app.route('/webhook', methods=['GET'])
def verifyweb():
        #Webhook verification
        return "Webhook verified", 200
        
@app.route('/webhook', methods=['POST'])
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

def processRequest(req):
    if req.get("result").get("action") != "findBranchLink":
        return {}
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
        app.run(debug = False, port = port, host = '0.0.0.0')
        
        
    
    '''baseurl = "https://query.yahooapis.com/v1/public/yql?"
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
    }'''
