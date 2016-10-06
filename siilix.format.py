import sys

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-i" in sys.argv:
    inputFile = getOptionValue("-i")
else:
    print "no"
    sys.exit()

familyNumber=1

with open(inputFile) as f:
    for line in f:
        #print line


        row = line.split()
        for i in range(len(row)):
            #if len(row)>14:
            print "FAM"+str(familyNumber),row[i]

        familyNumber+=1
