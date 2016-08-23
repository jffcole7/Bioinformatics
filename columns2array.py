#!/usr/bin/python

import csv
import sys



calls_table = []


def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue


if "-i" in sys.argv:
    fileName = getOptionValue("-i")
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()

with open(fileName) as f:
    reader = csv.reader(f, delimiter="\t")
    #reader = csv.reader(open(f,'rU'),delimiter="\t",dialect=csv.excel_tab)

    calls_table = list(reader)

# print calls_table[0][0]
# print calls_table[0][1]
# print calls_table[1][0]
#print len(calls_table)
# print range(len(calls_table))
#
# print "\n"
numRows = len(calls_table)-1
totNuc =4*numRows
processedNuc =0

ABBA = True
BABA = True
ValNow=""
column1="same"
column2="stillthis"
column3="pleasebedifferent"
column4="donotshowup"

for row in range(len(calls_table)):

    #ABBA = True
    #BABA = True


    for column in range(len(calls_table[row])):
        if row == 0:
            break
        ValNow = calls_table[row][column]
        if ValNow=="N":
            print "This row has an N"
            #ABBA = False
            #BABA = False
            processedNuc=processedNuc+column +1
            break
        if column == 0:
            column1 = ValNow
        if column == 1:
            column2 = ValNow
            if column2 == column1:
                #ABBA ==False
                #BABA == False
                print column1+column2 +" are the same thing"
                processedNuc=processedNuc+2
                break

        #print column2

        if column == 2:
            column3 = ValNow
            if column3 != column1 and column3 != column2:
                print column1+column2+column3+"is not biallelic"
                processedNuc = processedNuc+3
                break

            if column3 == column2 and column3 != column1:
                BABA = False
                #print column1+column2+column3+"this could be abba"
                #print column3 +" is equal to " + column2 +" but not " + column1
            else:
                #print column1+column2+column3+"this could be baba"
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
percenProcessed = float(processedNuc)/float(totNuc)

print "there were ",totNuc, " to be processed"
print "we only had to process ", processedNuc
print "we only looked at ", percenProcessed
            # if BABA == False and column2==column3:



            # if column3 == column1 and column3 != column2:
                # ABBA = False
                # print column1+column2+column3+"this will not be abba"
                # print column3 + " is equal to " + column1 + " but not " + column2
            # if ABBA ==False:
                # print column1+column2+column3+"this will not be abba"
                # if BABA == False:
                    # print column1+column2+column3+"this will not be baba"
                    # if column2 == column3:
                        # break
                    # print column1+column2+column3+"this is not biallelic"
            #print column1+column2+column3

#print column1+column2+column3









#    if ABBA or BABA == True:
#        if calls_table[row][0]==calls_table[row][1]:
#            ABBA = False
#            BABA = False
#            print "Not this row "+calls_table[row][0]+calls_table[row][1]
#        if ABBA or BABA == True:
#            if calls_table[row][2]==calls_table[row][3]:
#                ABBA = False
#                BABA = False
#                print "Not this row either"+calls_table[row][2]+calls_table[row][3]
#

#    if ABBA or BABA == True:
#        print "Y?AY"


    #for column in range(len(calls_table[row])):
        #print calls_table[2][column]






#print "*******************************"
#for column in range(len(calls_table[2])):
    #print calls_table[2][column]

#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n"
#for row in range(len(calls_table)):
    #print calls_table[row][2]





#print range(calls_table)
#for row in

#insert amazing loop here
