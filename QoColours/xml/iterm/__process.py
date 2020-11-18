import json
import os
import colorsys
from random import seed, shuffle

seed(6)

files = [f for f in os.listdir("./") if f.endswith("json")]


def sanitise(inString):
    replacements = [("-", "_"), (" ", "_"), (",","")]
    outString = inString
    for replacement in replacements:
        outString = outString.replace(replacement[0], replacement[1])
    return outString.lower()


outString = ""
for f in files:
    with open(f, "r") as fo:
        scheme = json.load(fo)
    name = sanitise(scheme["name"])
    f = scheme["foreground"][1:].upper()
    b = scheme["background"][1:].upper()
    fr, fg, fb = [int(f[2*i:2*i+2], 16) for i in range(3)]
    br, bg, bb = [int(b[2*i:2*i+2], 16) for i in range(3)]
    fhsv = colorsys.rgb_to_hsv(fr, fg, fb)
    bhsv = colorsys.rgb_to_hsv(br, bg, bb)
    Accents = [scheme["red"], scheme["green"], scheme["blue"], scheme["yellow"], scheme["purple"], scheme["cyan"]]
    shuffle(Accents)
    if fhsv[2] > bhsv[2]:
        colours = [scheme["background"], scheme["foreground"]] + Accents + [scheme["brightWhite"], scheme["brightBlack"]]
    else:
        colours = [scheme["foreground"], scheme["background"]] + Accents + [scheme["brightWhite"], scheme["brightBlack"]]
    colours = [c[1:].upper() for c in colours]
    outString += "\\DefineColourScheme{" + name + "}{" + ", ".join(colours) + "}\n"
    # outString += "\subsubsection{\\texttt{" + sanitise(name).replace("_", "\\_") + "}}\n\\ColourChart{" + sanitise(name) + "}\n\\newpage\n"


with open("__outFile.tex", "w+") as outFile:
    outFile.write(outString)

print(outString)
