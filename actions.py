import utils

def makeWebhookResult(req):
    action = req.get("result").get("action")
    if action == "findBranchLink":
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
