G_OBJECT = {
    "mDictionary": {
        "dictNumber": 42
    },
    "mList": [0, 1, 2],
    "mString": "Hello World",
    "mNum": 65
}

def parseTheData(jsonObject):
    className = createClassName()
    initMethod = createInitMethod()
    initMembers = []
    getMethods = []
    setMethods = []

    for key in jsonObject:
        value = jsonObject[key]
        initMembers.append(createINITMember(key, value))
        getMethods.append(createGetMethod(key))
        setMethods.append(createSetMethod(key))

    writeTheData(className, initMethod, initMembers, getMethods, setMethods)
    return

def writeTheData(className, initMethod, initMembers, getMethods, setMethods):
    for i in initMembers:
        print(initMembers[i])
        print(getMethods[i])
        print(setMethods[i])


    return

def createClassName():
    return "class YourClassName:\n"

def createInitMethod():
    return "\tdef __init__(self):\n"


def createINITMember(key, value):
    return "\t\tself." + key + "\n"

def createGetMethod(key):
    string = "\tdef get" + key + "(self):\n"
    string += "\t\t return self." + key + "\n"
    return string

def createSetMethod(key):
    string = "\tdef set" + key + "(self):\n"
    string += "\t\t return self." + key + "\n"
    return string

def test():
    parseTheData(G_OBJECT)
    return
test()
