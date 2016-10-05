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


with open(inputFile) as f:
    for line in f:
        #print line


        row = line.split()
        print len(row)
        
