import re
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import json

def clamp(x):
  return int(max(0, min(x, 255)))

def rgbToHex(rgb):
    return "{0:02x}{1:02x}{2:02x}".format(clamp(rgb[0]), clamp(rgb[1]), clamp(rgb[2])).upper()

def sanitise(inString):
    replacements = [("-", "_"), (" ", "_"), (",","")]
    outString = inString
    for replacement in replacements:
        outString = outString.replace(replacement[0], replacement[1])
    return outString.lower()

imFmt = "png"

urls = ["https://www.pinterest.co.uk/pin/507217976757002992/","https://www.pinterest.co.uk/pin/507217976757002989/","https://www.pinterest.co.uk/pin/507217976757002984/","https://www.pinterest.co.uk/pin/507217976757002982/","https://www.pinterest.co.uk/pin/507217976757002981/","https://www.pinterest.co.uk/pin/507217976757002977/","https://www.pinterest.co.uk/pin/507217976757002973/","https://www.pinterest.co.uk/pin/507217976757002968/","https://www.pinterest.co.uk/pin/507217976757002963/","https://www.pinterest.co.uk/pin/725712927447144242/","https://www.pinterest.co.uk/pin/507217976757002943/","https://www.pinterest.co.uk/pin/507217976757002937/","https://www.pinterest.co.uk/pin/507217976757002931/","https://www.pinterest.co.uk/pin/507217976757002927/","https://www.pinterest.co.uk/pin/507217976757002916/","https://www.pinterest.co.uk/pin/507217976757002911/","https://www.pinterest.co.uk/pin/507217976757002869/","https://www.pinterest.co.uk/pin/507217976757002837/","https://www.pinterest.co.uk/pin/507217976757002827/","https://www.pinterest.co.uk/pin/507217976757002822/","https://www.pinterest.co.uk/pin/507217976757002811/","https://www.pinterest.co.uk/pin/507217976757002792/","https://www.pinterest.co.uk/pin/507217976757002785/","https://www.pinterest.co.uk/pin/507217976757002772/","https://www.pinterest.co.uk/pin/507217976757002761/","https://www.pinterest.co.uk/pin/507217976757002717/","https://www.pinterest.co.uk/pin/507217976757002702/","https://www.pinterest.co.uk/pin/507217976757002685/","https://www.pinterest.co.uk/pin/507217976757002668/","https://www.pinterest.co.uk/pin/507217976756937920/","https://www.pinterest.co.uk/pin/507217976756937860/","https://www.pinterest.co.uk/pin/507217976756937851/"]
names = ["waveform", "verve", "urban", "trek", "thatch", "technic", "solsctice", "slipstream", "pushpin", "perspective", "paper", "origin", "oriel", "opulent", "newsprint", "module", "equity", "elemental", "couture", "concourse", "composite", "clarity", "civic", "black tie", "austin", "aspect", "apothecary", "apex", "angeles", "adjacency", "greyscale", "office default"]

# names = ["office 2011","greyscale","adjacency","advantage","angeles","apothecary","austin","black tie","breeze","capital","civic","clarity","couture","elemental","essential","executive","infusion","inkwell","inspiration","kilter","median","module","newsprint","orbit","paper","perception","perspective","pixel","plaza","precedent","pushpin","revolution","saddle","sketchbook","sky","slipstream","soho","solstice","spectrum","story","summer","technic","tradition","travelouge","twilight","urban pop","venture","waveform"]
#
# names = [name for name, m in zip(names, [not(name in names2010) for name in names]) if m] # filter out names which have already been covered
# urls = ["https://www.pinterest.co.uk/pin/507217976764836916/", "https://www.pinterest.co.uk/pin/507217976764836899/", "https://www.pinterest.co.uk/pin/507217976764836877/", "https://www.pinterest.co.uk/pin/507217976764836874/", "https://www.pinterest.co.uk/pin/507217976764836863/", "https://www.pinterest.co.uk/pin/507217976764836860/", "https://www.pinterest.co.uk/pin/507217976764836823/", "https://www.pinterest.co.uk/pin/507217976764836817/", "https://www.pinterest.co.uk/pin/507217976764836814/", "https://www.pinterest.co.uk/pin/507217976764836811/", "https://www.pinterest.co.uk/pin/507217976764836809/", "https://www.pinterest.co.uk/pin/507217976764836795/", "https://www.pinterest.co.uk/pin/507217976764836788/", "https://www.pinterest.co.uk/pin/507217976764836782/", "https://www.pinterest.co.uk/pin/507217976764836775/", "https://www.pinterest.co.uk/pin/507217976764836769/", "https://www.pinterest.co.uk/pin/507217976764836755/", "https://www.pinterest.co.uk/pin/507217976764836744/", "https://www.pinterest.co.uk/pin/507217976764836734/", "https://www.pinterest.co.uk/pin/507217976764836722/", "https://www.pinterest.co.uk/pin/507217976764836708/", "https://www.pinterest.co.uk/pin/507217976764836699/", "https://www.pinterest.co.uk/pin/507217976764836693/", "https://www.pinterest.co.uk/pin/507217976764836688/", "https://www.pinterest.co.uk/pin/507217976764836681/", "https://www.pinterest.co.uk/pin/507217976764836656/", "https://www.pinterest.co.uk/pin/507217976764836647/", "https://www.pinterest.co.uk/pin/507217976764836629/", "https://www.pinterest.co.uk/pin/507217976764836625/", "https://www.pinterest.co.uk/pin/507217976764836614/", ]

# print("\n".join(names))
# print(len(names), len(urls))

def getThemeImages(urls, names):
    for url, name in zip(urls, names):
        os.system("wget {} -O {}.html".format(url, sanitise(name)))
        with open("{}.html".format(sanitise(name)), "r") as file:
            fileURL = re.search("https://i\.pinimg\.com/originals/.*?\.{}".format(imFmt), file.read()).group(0)
            print("\n\n\t\t" + fileURL + "\n\n")
            if fileURL:
                os.system("wget {} -O {}.{}".format(fileURL, sanitise(name), imFmt))
            else:
                print("Could not get file {}".format(sanitise(name)))
    os.system("rm ./*.html")

# getThemeImages(urls, names)

outString = ""
schemesDict  = {}

fileName = "./{}.{}".format(sanitise(names[0]), imFmt)

im = Image.open(fileName)
width, height = im.size

# plt.imshow(np.asarray(im))
# # plt.xticks(np.arange(0, width, step = 1))
# # plt.yticks(np.arange(0, height, step = 1))
# plt.grid(which = "both", axis = "both")
# plt.show()



for name in names:
    fileName = "./{}.{}".format(sanitise(name), imFmt)

    im = Image.open(fileName)
    ims = []

    width, height = im.size
    if imFmt == "jpg":
        left = 176
        right = 180
        top = 480
        bottom = 495
        width = 237 - 172
    else:
        left = 226
        right = 300
        top = 660
        bottom = 663
        width = 312 - 226
    for i in range(0,8):
        ims.append(im.crop((left + width * i, top, right + width * i, bottom)))
    cols = []
    for im in ims:
        avg_color_per_row = np.average(np.asarray(im), axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        cols.append(rgbToHex(avg_color[0:-1] if imFmt == "png" else avg_color))
    cols += ["0000FF", "00AA00"]
    cols = [cols[1], cols[0]] + cols[2:]

    # outString += "\\DefineColourScheme{" + sanitise(name) + "}{" + ", ".join(cols) + "}\n"
    schemesDict[name] = cols
    # outString += "\section{" + sanitise(name).replace("_", "\\_") + "}\n\\ColourChart{" + sanitise(name) + "}\n\\newpage\n"
#
# with open("outFilePinterest.tex", "w+") as outFile:
#     outFile.write(outString)
#
with open("colourSchemesFullPinterest.json", "w+") as jsonFile:
    json.dump(schemesDict, jsonFile, indent = 4)
