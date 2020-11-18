import json

def sanitise(inString):
    replacements = [("-", "_"), (" ", "_"), (",","")]
    outString = inString
    for replacement in replacements:
        outString = outString.replace(replacement[0], replacement[1])
    return outString.lower()

coloursFilePath = "./colourSchemes.json"

with open(coloursFilePath, "r") as coloursFile:
    colourSchemes = json.load(coloursFile)

outString = ""

# for scheme, variants in colourSchemes.items():
#     for variant, colours in variants.items():
#         # outString += "\\DefineColourScheme{" + sanitise(scheme) + "__" + sanitise(variant) + "}{" + ", ".join(colours) + "}\n"
#         outString += "\section{" + sanitise(scheme).replace("_", "\\_") + "\\_\\_" + sanitise(variant).replace("_", "\\_") + "}\n\\ColourChart{" + sanitise(scheme) + "__" + sanitise(variant) + "}\n\\newpage\n"
# with open("outFile.tex", "w+") as outFile:
#     outFile.write(outString)


for scheme, variants in sorted(colourSchemes.items()):
    if "Light" in variants:
        variant = "Light"
        colours = variants[variant]
        # outString += "\\DefineColourScheme{" + sanitise(scheme) + "}{" + ", ".join(colours) + "}\n"
        outString += "\section{" + sanitise(scheme).replace("_", "\\_") + "}\n\\ColourChart{" + sanitise(scheme) + "}\n\\newpage\n"
with open("outFile.tex", "w+") as outFile:
    outFile.write(outString)
