#import WriteInFIle
import codecs as c
def writeInFile(filename, filecontent, operationtype):
    if(operationtype == 0):
        outfile = open(filename, "w")
    elif(operationtype == 1):
        outfile = open(filename, "a")
    outfile.write(str(filecontent))

    outfile.close()




data = []
lines = c.open("dataset/182.txt", "r", "utf-8")
for line in lines:
    data.append(line)
i = 0
while i < len(data)-1:
    writeInFile("dataset/phrases.txt", data[i], 1)
    writeInFile("dataset/paraphrases.txt", data[i+1], 1)
    i = i + 2