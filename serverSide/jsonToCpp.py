import jsonToPyDict

G_OBJECT = jsonToPyDict.jsonToPyDict("object.json")
variableTypes= {"<class 'dict'>":"std::map<char, char>",
"<class 'list'>":"int",
"<class 'str'>":"char",
"<class 'int'>":"int",
"<class 'bool'>":"bool",
"<class 'NoneType'>":"int*"}

print(G_OBJECT)

def parseTheData(jsonObject):
    className = createClassName()
    
    initMembers = []
    getMethods = []
    setMethods = []

    for key in jsonObject:
        value = jsonObject[key]
        dtype = type(value)
        ctype = variableTypes[str(dtype)]
        initMembers.append(ctype +" "+ key+";")

    print(initMembers)
    return

def writeTheData(className, privateAndpublic, initMembers, getMethods, setMethods):
    cppFile = open("yourClass.cpp", "w")
    cppFile.write("#include <map>\n")
    cppFile.write(className)
    cppFile.write("{\nprivate:\n")
    for i in range(len(initMembers)):
        cppFile.write(initMembers[i])
    
    for i in range(len(getMethods)):
        cppFile.write(getMethods[i])
        cppFile.write(setMethods[i])
    return

def createClassName():
    return "class YourClassName\n"




def test():
    parseTheData(G_OBJECT)
    return

test()