import urllib
import json 

import os
import sys

from flask import Flask
from flask import request
from flask import make_response

import utils

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
