#line = "TR13336|c0_g1 GO:0003674,GO:0003824,GO:0005215"

import sys

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-i" in sys.argv:
    go_file = getOptionValue("-i")
else:
    print "no"
    sys.exit()

    
with open(go_file) as f:
    for line in f:
        row = line.split()
        go = row[1].split(",")
        for i in range(len(go)):
            print row[0] +"\t"+ go[i]



#
            #
        # print row[0]
        # if row[0] in index_array:
            # print line
# go= line.split()[1]
# print go.split(",")
