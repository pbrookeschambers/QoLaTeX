import re



fileName = "./QoColours/qocolours.sty"

with open(fileName, "r") as file:
    contents = file.read().split("\n")

while contents[0] == "":
    contents = contents[1:]

while contents[-1] == "":
    contents = contents[:-1]

schemeNames = []

for line in contents:
    if line.strip().startswith("\\DefineColourScheme"):
        match = re.search("(?<=DefineColourScheme{).*?(?=})", line)
        schemeNames.append(match.group(0).strip())

# for name in schemeNames:
#     print(f"_{name}_")

length = len(sorted(schemeNames, key = len)[-1]) + 5

outString = ""

for line in contents:
    if line.strip().startswith("\\DefineColourScheme"):
        match = re.search("(?<=DefineColourScheme{)(.*?)(?:\s*}\s*{\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*,\s*)([0-9a-zA-z]*?)(?:\s*})", line)
        codes = ",            ".join([match.group(i).upper() for i in range(2, 12)]) + "           "
        pad = length - int(len(line) - len(line.lstrip(" ")))
        l = " " * int(len(line) - len(line.lstrip(" "))) + f"\\DefineColourScheme{{{match.group(1)}}}" + ' ' * int(pad - len(match.group(1))) + f"{{{codes}}}"
        # l = f"\\DefineColourScheme{{{match.group(1)}}}{{{match.group(2)}, {match.group(3)}, {match.group(4)}, {match.group(5)}, {match.group(6)}, {match.group(7)}, {match.group(8)}, {match.group(9)}, {match.group(10)}, {match.group(11)}}}"
        # print(l)
    else:
        l = line

    outString += l + "\n"

with open(fileName, "w") as outFile:
    outFile.write(outString)
