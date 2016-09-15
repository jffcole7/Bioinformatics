import sys

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue


if "-id" in sys.argv:
    index_file = getOptionValue("-id")
else:
    print "no id"
    sys.exit()

if "-go" in sys.argv:
    go_file = getOptionValue("-go")
else:
    print "no id"
    sys.exit()
index_array = []

with open(index_file) as f:
    for line in f:
        line = line.split()
        if line != "":
            index_array.append(line)
#print index_array
with open(go_file) as f:
    for line in f:
        row = line.split()
        print row[0]
        if row[0] in index_array:
            print line
