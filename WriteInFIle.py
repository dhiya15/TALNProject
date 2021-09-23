def writeInFile(filename, filecontent, operationtype):
    if(operationtype == 0):
        outfile = open(filename, "w")
    elif(operationtype == 1):
        outfile = open(filename, "a")
    outfile.write(str(filecontent))
    outfile.write("\n")
    outfile.close()