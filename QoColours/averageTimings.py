import re

file = "schemesLightCompileLog.log"

with open(file, "r") as f:
	contents = f.read()

drawTimes = re.findall("(?<=drawing chart:\s)[0-9\.]*(?=sec)", contents)
loadTimes = re.findall("(?<=loading scheme:\s)[0-9\.]*(?=sec)", contents)
for i in range(len(loadTimes)):
	drawTimes[i] = float(drawTimes[i])
	loadTimes[i] = float(loadTimes[i])
print("Average load time: {:.5f}".format(sum(loadTimes) / len(loadTimes)))
print("Average draw time: {:.5f}".format(sum(drawTimes) / len(drawTimes)))
