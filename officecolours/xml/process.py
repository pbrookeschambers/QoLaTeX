import untangle as un
import os
import json

fileName = "./Aspect.xml"

def sanitise(inString):
    replacements = [("-", "_"), (" ", "_"), (",","")]
    outString = inString
    for replacement in replacements:
        outString = outString.replace(replacement[0], replacement[1])
    return outString.lower()

def getSchemeColours(fileName):
    xml = un.parse(fileName)
    colNames = ["dk2","lt2","accent1","accent2","accent3","accent4","accent5","accent6","hlink","folHlink"]
    scheme = []
    for name in colNames:
        scheme.append(eval("xml.a_clrScheme.a_" + name + ".a_srgbClr['val']"))
    name = xml.a_clrScheme["name"]
    return sanitise(name), tuple(scheme)

schemesDict = {}


outString = ""

for fileName in os.listdir("./"):
    if fileName.endswith(".xml"):
        scheme, colours = getSchemeColours(fileName)
        outString += "\\DefineColourScheme{" + sanitise(scheme) + "}{" + ", ".join(colours) + "}\n"
        schemesDict[scheme] = colours
        # outString += "\section{" + sanitise(scheme).replace("_", "\\_") + "}\n\\ColourChart{" + sanitise(scheme) + "}\n\\newpage\n"

with open("outFile.tex", "w+") as outFile:
    outFile.write(outString)

with open("colourSchemesFull.json", "w+") as jsonFile:
    json.dump(schemesDict, jsonFile, indent = 4)
