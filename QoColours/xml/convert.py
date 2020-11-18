import colorsys
import json

def hexToHsb(hex):
    ep = 1E-5                   # The lower bound at which the range is considered 0
    r = int(hex[0:2], 16) / 255
    g = int(hex[2:4], 16) / 255
    b = int(hex[4:], 16) / 255
    rgbmin = min(r, g, b)
    rgbmax = max(r, g, b)
    rgbrange = rgbmax - rgbmin
    v = rgbmax
    if rgbrange < ep or v == 0: # If the colour is grey or black
        return (0, 0, v)
    if v > 0:
        s = rgbrange / v
    if r == rgbmax:             # If the colour is between yellow and magenta
        h = (g - b) / rgbrange
    elif g == rgbmax:           # If the colour is between cyan and yellow
        h = 2 + (b - r) / rgbrange
    else:                       # If the colour is between magenta and cyan
        h = 4 + (r - g) / rgbrange
    h = h / 6                   # Bring h to the range [0,1]
    if h < 0:
        h += 1                  # If h is negative, wrap around to positive.
    return (h, s, v)

def hexToHsl(hex):
    r = int(hex[0:2], 16) / 255
    g = int(hex[2:4], 16) / 255
    b = int(hex[4:], 16) / 255
    hls = colorsys.rgb_to_hls(r, g, b)
    return (hls[0]*360, hls[2], hls[1])

print(hexToHsl("8f598b"))


# with open("colourSchemesFull.json", "r") as jsonFile:
#     schemes = json.load(jsonFile)
#
# outFile = "./colourSchemesFullHSB.json"
# for scheme, colours in schemes.items():
#     schemes[scheme] = [list(hexToHsb(c)) for c in colours]
#
# with open(outFile, "w+") as outJsonFile:
#     json.dump(schemes, outJsonFile, indent = 4)
