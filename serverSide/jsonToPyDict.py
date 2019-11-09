import json

def jsonToPyDict(filename):
    jsonFile = open(filename)
    jsonData = jsonFile.read()
    # print(jsonData)
    jsonLoad = json.loads(jsonData)
    # print(jsonLoad)
    return jsonLoad

# jsonToPyDict("object.json")