import jsonToPyDict

def parseTheData(jsonObject, classNameP = "YourClassName", filename = "yourFilename.py"):
    className = createClassName(classNameP)
    initMethod = createInitMethod()
    populatedInitMethod = createPopulatedInit(jsonObject)
    splitInitAndMethods = "\t\treturn\n\n"
    initMembers = []
    getMethods = []
    setMethods = []

    for key in jsonObject:
        value = jsonObject[key]
        initMembers.append(createINITMember(key, value))
        getMethods.append(createGetMethod(key))
        setMethods.append(createSetMethod(key))

    writeTheData(className, initMethod, splitInitAndMethods, populatedInitMethod, initMembers, getMethods, setMethods, filename)
    return

def createPopulatedInit(jsonObject):
    string = "\tdef __init__(self"
    for key in jsonObject:
        string += ", v" + key
    string += "):\n"
    for key in jsonObject:
        string += "\t\tself." + key + " = v" + key + '\n'
    return string


def writeTheData(className, initMethod, splitInitAndMethods, populatedInitMethod, initMembers, getMethods, setMethods, filename):
    pythonFile = open(filename, "w")
    pythonFile.write(className)
    pythonFile.write(initMethod)
    for i in range(len(initMembers)):
        pythonFile.write(initMembers[i])

    pythonFile.write(splitInitAndMethods)
    pythonFile.write(populatedInitMethod)
    pythonFile.write(splitInitAndMethods)
    
    for i in range(len(getMethods)):
        pythonFile.write(getMethods[i])
        pythonFile.write(setMethods[i])
    return

def createClassName(classnameP):
    return "class "+classnameP+":\n\n"

def createInitMethod():
    return "\tdef __init__(self):\n"


def createINITMember(key, value):
    if type(value) == str:
        return "\t\tself." + key + " = " + '"' + str(value) + '"' + "\n"
    return "\t\tself." + key + " = " + str(value) + "\n"

def createGetMethod(key):
    string = "\tdef get" + key + "(self):\n"
    string += "\t\treturn self." + key + "\n\n"
    return string

def createSetMethod(key):
    string = "\tdef set" + key + "(self, value):\n"
    string += "\t\tself." + key + " = value\n"
    string += "\t\treturn\n\n"
    return string
