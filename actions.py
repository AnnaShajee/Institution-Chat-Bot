import urllib
import json 

import os
import sys

from flask import Flask
from flask import request
from flask import make_response

from utils import *

def makeWebhookResult(req):
    action = req.get("result").get("action")
    context = req.get("result").get("context")
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
    elif action == "findLeader":
        result = findLeader(req)
    elif context[0]['name'] =="dean":
        result = findDean(req)
    else:
        result = default()
    print(result)
    return result
