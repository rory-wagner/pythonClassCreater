import json

def jsonToPyDict(filename):
    jsonFile = open(filename)
    jsonData = jsonFile.read()
    jsonLoad = json.loads(jsonData)
    return jsonLoad
