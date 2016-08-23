import sys

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue


if "-i" in sys.argv:
    fileName = getOptionValue("-i")
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()
column1=""
column2=""
column3=""
column4=""
line1=True
with open(fileName) as f:
    for line in f:
        #print line
        if line1:
            line1=False
            continue
        row = line.split()

        #print len(row)
        for column in range(len(row)):


            newVal=row[column]
            if column == 0:
                column1 = newVal
            if column == 1:
                column2 = newVal
            if column == 2:
                column3 = newVal
            if column == 3:
                column4 = newVal
        print column1+column2+column3+column4

        # for column in range(len(row)):
            # newVal = row[column]
            # print newVal
