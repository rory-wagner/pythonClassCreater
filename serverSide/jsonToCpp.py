import jsonToPyDict

G_OBJECT = jsonToPyDict.jsonToPyDict("object.json")
variableTypes= {"<class 'dict'>":"std::map<char, char>",
"<class 'list'>":"int",
"<class 'str'>":"char",
"<class 'int'>":"int",
"<class 'bool'>":"bool",
"<class 'NoneType'>":"int*"}



def parseTheData(jsonObject):
    className = createClassName()
    # type and variable name
    initMembers = []
    #get methods
    getMethods = []
    #set methods
    setMethods = []
    #print publics
    publics = []
    #value types
    ctypes = []
    #init setters
    dataMembers = []
    values = []
    count = 0
    for key in jsonObject:
        value = jsonObject[key]
        values.append(value)
        dtype = type(value)
        ctype = variableTypes[str(dtype)]
        ctypes.append(ctype)
        initMembers.append("\t"+ ctype +" "+ key+";\n")
        getMethods.append(ctype+ " "+ className+"::get"+key+"(){\n\treturn "+key+";\n}\n")
        publics.append("\t"+ctype+" get"+key+"();\n\tvoid set"+key+"("+ctype+" value);\n")
        dataMembers.append("\t"+key+" = value"+str(count)+";\n")
        count +=1
        setMethods.append("void "+className+"::set"+key+"("+ctype+" value){\n\t"+key+" = value;\n}\n")
    writeTheData(className, dataMembers, initMembers, getMethods, setMethods, publics, ctypes, values)
    return

def writeTheData(className, dataMembers, initMembers, getMethods, setMethods, publics, ctypes, values):
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
            string=ctypes[i]+" "+"value"+str(i) +", "
        else:
             string=ctypes[i]+" "+"value"+str(i)
        valuesAll+=string
    cppFile.write("\t"+className+"();\n\t"+className+"("+valuesAll+")\n\t~"+className+"();\n};\n\n")

    
    for i in range(len(getMethods)):
        cppFile.write(getMethods[i])
        cppFile.write(setMethods[i])

    valuesAll = ""
    for i in range(len(ctypes)):
        if ctypes[i] == 'std::map<char, char>':
            dic = values[i]
            setted = "{\n"
            lst = []
            for key in dic:
                lst.append([key, dic[key]])
            for j in range(len(lst)):
                if j <len(lst)-1:
                    t = lst[j]
                    setted+="\t{'"+str(t[0])+"', '"+str(t[1])+"'},\n"
                else:
                    t = lst[j]
                    setted+="\t{'"+str(t[0])+"', '"+str(int(t[1]))+"'}\n};"
            
        elif ctypes[i] == 'int':
            setted  = values[i]
            if isinstance(setted, list):
                
                array = "{"
                for j in range(len(setted)):
                    if j < len(setted)-1:
                        array+=str(setted[j])
                        array+=", "
                    else:
                        array+=str(setted[j])
                array += "}"
                setted = array
        elif ctypes[i] == 'char':
            setted = "'"+str(values[i])+"'"
        elif ctypes[i] == 'bool':
            if values[i]:
                setted = "true"
            else:
                setted = "false"
        elif ctypes[i] == 'int*':
            
            if values[i] is None:
                setted ="null"
            else:
                setted = str(values[i])
        if i < len(ctypes)-1:
            temp = ", "         
        else:
            temp = ""       
        string=ctypes[i]+" "+"value"+str(i) +" = "+ str(setted)+temp
        # else:
        #     string=ctypes[i]+" "+"value"+str(i) + " = "+ str(values[i])
        valuesAll+=string

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

#test()