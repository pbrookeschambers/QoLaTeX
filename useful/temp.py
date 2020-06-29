import json

with open("./colourSchemes.json", 'r') as s:
    schemes = json.load(s)

outString = ""

colourOrder = ["BackgroundColour", "ForegroundColour", "Accent1", "Accent2", "Accent3", "Accent4", "Accent5"]

perLine = 5

for schemeName, scheme in schemes.items():
    outString += r"\subsection*{" + schemeName + "}\n"
    for variantName, variant in scheme.items():
        outString += r"\subsubsection*{" + variantName + "}\n"
        outString += r"\noindent\begin{tikzpicture}" + "\n"
        for i, colour in enumerate(variant):
            outString += r"\definecolor{col}{HTML}{" + colour + "}\n"
            outString += r"\fill[col] " + \
            "(" + str((i % perLine) * 3.5) + ", -0.5em + " + str(-3 if i >= perLine else 0) + "em) " +\
            "rectangle " +\
            "(" + str((i % perLine) * 3.5 + 2) + ", 1em + " + str(-3 if i >= perLine else 0) + "em) " +\
            "(" + str((i % perLine) * 3.5 + 1) + ", 1em + " + str(-3 if i >= perLine else 0) + "em) " +\
            "node[above, text = black] {" + colourOrder[i] + "};\n"
        # Accent Text Colour
        i += 1
        outString += r"\definecolor{col}{HTML}{" + variant[0] + "}\n"
        outString += r"\fill[col!50!" + ("white" if variantName == "Light" else "black") + "] " + \
        "(" + str((i % perLine) * 3.5) + ", -0.5em + " + str(-3 if i >= perLine else 0) + "em) " +\
        "rectangle " +\
        "(" + str((i % perLine) * 3.5 + 2) + ", 1em + " + str(-3 if i >= perLine else 0) + "em) " +\
        "(" + str((i % perLine) * 3.5 + 1) + ", 1em + " + str(-3 if i >= perLine else 0) + "em) " +\
        "node[above, text = black] {AccentTextColour};\n"
        # Dark Text Colour
        i += 1
        outString += r"\definecolor{col}{HTML}{" + variant[1 if variantName == "Light" else 0] + "}\n"
        outString += r"\fill[col" + ("!50!black" if variantName == "Dark" else "") + "] " + \
        "(" + str((i % perLine) * 3.5) + ", -0.5em + " + str(-3 if i >= perLine else 0) + "em) " +\
        "rectangle " +\
        "(" + str((i % perLine) * 3.5 + 2) + ", 1em + " + str(-3 if i >= perLine else 0) + "em) " +\
        "(" + str((i % perLine) * 3.5 + 1) + ", 1em + " + str(-3 if i >= perLine else 0) + "em) " +\
        "node[above, text = black] {DarkTextColour};\n"
        outString += r"\end{tikzpicture}" + "\n\n"

print(outString)

outString = ""
for schemeName, scheme in schemes.items():
    if not("Light" in scheme):
        scheme["Light"] = scheme["Dark"].copy()
        scheme["Light"][0] = scheme["Dark"][1]
        scheme["Light"][1] = scheme["Dark"][0]
    if not("Dark" in scheme):
        scheme["Dark"] = scheme["Light"].copy()
        scheme["Dark"][0] = scheme["Light"][1]
        scheme["Dark"][1] = scheme["Light"][0]
    outString += r"\DeclareOption{" + schemeName.lower().replace(" ","") + "} {\n"
    for variantName, variant in scheme.items():
        for i, colour in enumerate(variant):
            outString += "\t" + r"\definecolor{" + variantName + colourOrder[i] + "}{HTML}{" + colour + "}\n"
    outString += "}\n\n"

# print(outString)
