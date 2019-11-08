import jsonToPyDict

#G_OBJECT = jsonToPyDict.jsonToPyDict("object.json")

def parseTheData(jsonObject):
    className = createClassName()
    initMethod = createInitMethod()
    splitInitAndMethods = "\t\treturn\n"
    initMembers = []
    getMethods = []
    setMethods = []

    for key in jsonObject:
        value = jsonObject[key]
        initMembers.append(createINITMember(key, value))
        getMethods.append(createGetMethod(key))
        setMethods.append(createSetMethod(key))

    writeTheData(className, initMethod, splitInitAndMethods, initMembers, getMethods, setMethods)
    return

def writeTheData(className, initMethod, splitInitAndMethods, initMembers, getMethods, setMethods):
    pythonFile = open("yourClass.py", "w")
    pythonFile.write(className)
    pythonFile.write(initMethod)
    for i in range(len(initMembers)):
        pythonFile.write(initMembers[i])
    
    for i in range(len(getMethods)):
        pythonFile.write(getMethods[i])
        pythonFile.write(setMethods[i])
    return

def createClassName():
    return "class YourClassName:\n"

def createInitMethod():
    return "\tdef __init__(self):\n"


def createINITMember(key, value):
    return "\t\tself." + key + "\n"

def createGetMethod(key):
    string = "\tdef get" + key + "(self):\n"
    string += "\t\treturn self." + key + "\n"
    return string

def createSetMethod(key):
    string = "\tdef set" + key + "(self, value):\n"
    string += "\t\tself." + key + " = value\n"
    string += "\t\treturn\n"
    return string

# def test():
#     parseTheData(G_OBJECT)
#     return
# test()
