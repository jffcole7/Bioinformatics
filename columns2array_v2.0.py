#!/usr/bin/python

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

numRows = 0
#totNuc =4*numRows
processedNuc =0

ABBA = True
BABA = True
ValNow=""
column1="same"
column2="stillthis"
column3="pleasebedifferent"
column4="donotshowup"
line1=True


with open(fileName) as f:
    for line in f:
        if line1:
            line1=False
            continue

        row = line.split()
        numRows +=1







        for column in range(len(row)):

            ValNow = row[column]
            if ValNow=="N":
                print "This row has an N"

                processedNuc=processedNuc+column +1
                break
            if column == 0:
                column1 = ValNow
            if column == 1:
                column2 = ValNow
                if column2 == column1:

                    print column1+column2 +" are the same thing"
                    processedNuc=processedNuc+2
                    break



            if column == 2:
                column3 = ValNow
                if column3 != column1 and column3 != column2:
                    print column1+column2+column3+"is not biallelic"
                    processedNuc = processedNuc+3
                    break

                if column3 == column2 and column3 != column1:
                    BABA = False

                else:
                    ABBA = False
            if column == 3:
                column4 = ValNow
                if column4==column3:
                    print column1+column2+column3+column4+" You will not be goingto space today "
                    break
                    processedNuc=processedNuc+4
                if column4!=column1 and column4!=column2:
                    print column1+column2+column3+column4+" There is an extra letter in here "
                    processedNuc=processedNuc+4
                    break

                if column4 == column1:
                    print column1+column2+column3+column4+" This is ABBA!!!!! "
                    processedNuc=processedNuc+4
                else:
                    print column1+column2+column3+column4+" This is BABA!!!!! "
                    processedNuc=processedNuc+4
totNuc = 4*numRows
percenProcessed = float(processedNuc)/float(totNuc)

print "there were ",totNuc, " to be processed"
print "we only had to process ", processedNuc
print "we only looked at ", percenProcessed
            # if BABA == False and column2==column3:
