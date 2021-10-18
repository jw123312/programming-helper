import pyperclip

def preprocess():
    a = pyperclip.paste()
    a = a.replace("private", "")
    a = a.replace(";", "").replace("\t", "")
    a = a.replace("\r", "")
    var = a.split("\n")

    var = [i.strip() for i in var if i.strip() != '' and i.strip()[0] != "@"]
    return var

def constructor():
    var = preprocess()

    text = "("
    for i in var[:len(var)-1]:
        typ = i.split()[0]
        name = i.split()[1]
        text += f"{typ} {name}, "

    typ = var[len(var)-1].split()[0]
    name = var[len(var)-1].split()[1]
    text += f"{typ} {name}"
    
    text = text + ") {\n"

    
    for i in var:
        typ = i.split()[0]
        name = i.split()[1]
        text+= f"\tthis.{name} = {name};\n"
    
 
    
    text = text + "\t}"
    pyperclip.copy(text)

def getsetmethod():
    strs = []
    
    var = preprocess()
    
    for i in var:
        if (i == ""):
            continue
        
        typ = i.split()[0]
        name = i.split()[1]

        name = name[0].upper() + name[1:]
        
        #get
        strs.append("public " + typ +" get"+ name + "() {\n\t return " +i.split()[1] +";\n}")

        #set
        strs.append("public void set" + name + "(" + i + ") {\n\tthis." + i.split()[1]+ " = " + i.split()[1] + ";\n}")

    strings = "\n\n".join(strs)
    pyperclip.copy(strings)

def tostringmethod():
    var = preprocess()
    text = "@Override\n\tpublic String toString() {\n\t\treturn "
    
    for i in var[:len(var)-1]:
        if (i == ""):
            continue
        
        typ = i.split()[0]
        name = i.split()[1]

        name = name[0].upper() + name[1:]
        text = text + f"\"{name}=\" + {i.split()[1]} + \", \" +\n\t\t\t"

    i = var[len(var)-1]
    typ = i.split()[0]
    name = i.split()[1]

    name = name[0].upper() + name[1:]
    text = text + f"\"{name}=\" + {i.split()[1]};\n"
    text = text + "\t}"
    pyperclip.copy(text)
  

    
