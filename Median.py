import csv

file = open("124.csv", newline = "")
reader = csv.reader(file)
filedata = list(reader)
filedata.pop(0)
newData = []

for i in range(len(filedata)):
    num = filedata[i][2]
    newData.append(float(num))

n = len(newData)
newData.sort()

if n % 2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 - 1])
    median = (median1 + median2) / 2
else :
    median = newData[n//2]
    print(n)

print("Median Is : " + str(median))
