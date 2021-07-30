import csv
from collections import Counter

file = open("124.csv", newline = "")
reader = csv.reader(file)

filedata = list(reader)
filedata.pop(0)

newdata = []
for i in range(len(filedata)):
    number = filedata[i][2]
    newdata.append(float(number))

data = Counter(newdata)
rangedata = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for height,occurence in data.items():
    if(75<float(height)<85):
        rangedata["75-85"]+=occurence 
    elif(85<float(height)<95):
        rangedata["85-95"]+=occurence
    elif(95<float(height)<105):
        rangedata["95-105"]+=occurence
    elif(105<float(height)<115):
        rangedata["105-115"]+=occurence 
    elif(115<float(height)<125):
        rangedata["115-125"]+=occurence
    elif(125<float(height)<135):
        rangedata["125-135"]+=occurence
    elif(135<float(height)<145):
        rangedata["135-145"]+=occurence 
    elif(145<float(height)<155):
        rangedata["145-155"]+=occurence
    elif(155<float(height)<165):
        rangedata["155-165"]+=occurence
    elif(165<float(height)<175):
        rangedata["165-175"]+=occurence

moderange,modeoccurence = 0,0
for range,occurence in rangedata.items():
    if(occurence>modeoccurence):
        moderange,modeoccurence = [int(range.split("-")[0]), int(range.split("-")[1])],occurence

mode = float((moderange[0]+moderange[1])/2)

print("Mode Is : " + str(mode))
