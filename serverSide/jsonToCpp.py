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
    publics = []
    ctypes = []
    dataMembers = []
    count = 0
    for key in jsonObject:
        value = jsonObject[key]
        dtype = type(value)
        ctype = variableTypes[str(dtype)]
        ctypes.append(ctype)
        initMembers.append("\t"+ ctype +" "+ key+";\n")
        getMethods.append(ctype+ " "+ className+"::get"+key+"(){\n\treturn "+key+";\n}\n")
        publics.append("\t"+ctype+" get"+key+"();\n\tvoid set"+key+"("+ctype+" value);\n")
        dataMembers.append("\t"+key+" = value"+str(count)+";\n")
        count +=1
        setMethods.append("void "+className+"::set"+key+"("+ctype+" value){\n\t"+key+" = value;\n}\n")
    writeTheData(className, dataMembers, initMembers, getMethods, setMethods, publics, ctypes)
    return

def writeTheData(className, dataMembers, initMembers, getMethods, setMethods, publics, ctypes):
    cppFile = open("yourClass.cpp", "w")
    cppFile.write("#include <map>\n")
    cppFile.write("class "+className+"\n")
    cppFile.write("{\nprivate:\n")
    for i in range(len(initMembers)):
        cppFile.write(initMembers[i])
    cppFile.write("public:\n")
    for i in range(len(publics)):
        cppFile.write(publics[i])
    valuesAll = ""
    for i in range(len(ctypes)):
        if i < len(ctypes)-1:
            string=ctypes[i]+" "+"value"+str(i)+", "
        else:
             string=ctypes[i]+" "+"value"+str(i)
        valuesAll+=string
    cppFile.write("\t"+className+"();\n\t"+className+"("+valuesAll+")\n\t~"+className+"();\n};\n\n")

    
    for i in range(len(getMethods)):
        cppFile.write(getMethods[i])
        cppFile.write(setMethods[i])

    cppFile.write(className+"::"+className+"()\n{\n\n}\n\n"+className+"::"+className+"("+valuesAll+")\n{\n")
    for i in range(len(dataMembers)):
        cppFile.write(dataMembers[i])
    cppFile.write("\n}\n\n"+className+"::~"+className+"()\n{\n\n}")
    return

def createClassName():
    return "YourClassName"




def test():
    parseTheData(G_OBJECT)
    return

test()