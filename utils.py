import json

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
