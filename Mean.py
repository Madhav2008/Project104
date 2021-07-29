import csv

file = open("124.csv", newline = "")
reader = csv.reader(file)

filedata = list(reader)
filedata.pop(0)

newdata = []

for i in range(len(filedata)):
    number = filedata[i][2]
    newdata.append(float(number))

n = len(newdata)
total = 0

for i in newdata:
    total = total + i

mean = total / n

print("Mean Is : " + str(mean))
