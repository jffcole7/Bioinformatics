#!/usr/bin/python

import sys
from scipy.stats import chi2






def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue



def chi2_test(val0, val1):
    """Calculate Pearson Chi-Squared for the special case of
       two values that are expected to be equal
       Arguments:
           val0: first value
           val1: second value
    """
    try:
        chisq = float((val0 - val1)**2) / float(val0 + val1)
        if not chisq:
            return (0, 1)
        pval = 1.0 - chi2.cdf(chisq, 1)
        return (chisq, pval)
    except ZeroDivisionError as errstr:
        return (0, 1)

def dstat(val0,val1):
    try:

        Dstat = float(val0 - val1)/float(val0+val1)
        return Dstat
    except ZeroDivisionError as errstr:
        return 0



if "-i" in sys.argv:
    fileName = getOptionValue("-i")
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()


    #
if "-o" in sys.argv:
  outName = getOptionValue("-o")
  #out = open(outName, "w")
else:
  print "\nplease specify output file name using -o <file_name> \n"
  sys.exit()

if "-w" in sys.argv:
    winSize = float(getOptionValue("-w"))
else:
    print "\nplease specify window size using -w <window size> \n"
    sys.exit()

with open(outName,'wb') as out:
        out.write("chrom\tblockRange\tABBA\tBABA\tDstat\tDcube\tChisq\tP-val\n")
#
#

def unique_count(thing):

    uniq_char_string=''.join(set(thing))
    uniq_char_count = len(uniq_char_string)
    return uniq_char_count




numRows = 0
#totNuc =4*numRows
processedNuc =0

ABBA_bool = True
BABA_bool = True

AABA=0
ABAA=0
ABBA=0
BAAA=0
BABA=0
BBAA=0
BBBA=0
Other=0
Ncount=0
N1=0
N2=0
N3=0
N4=0

D_stat = 0
D_cube=0

ValNow=""
column1="same"
column2="stillthis"
column3="pleasebedifferent"
column4="donotshowup"
line1=True
start_pos =1
prev_pos=start_pos
#abbaMatrix=[]
#abbaMatrix.append(['chrom','pos','ABBA'])
chrom = "1"
pos = ""
#block=[]
blockNum =1
row =[]
alleles=""
#chrom_change=""
#print "chrom\tpos\tAABA\tABAA\tABBA\tBAAA\tBABA\tBBAA\tBBBA"
#print abbaMatrix
def Dcount(row):
    for column in range(len(row)):
        chrom_change = chrom
        chrom = row[0]


        pos = int(float(row [1]))
        ValNow = row[column]
        if ValNow=="N":
            #print "This row has an N"


            # Other+=1
            # Ncount+=1
            # if column == 2:
                # N1+=1
            # if column == 3:
                # N2+=1
            # if column == 4:
                # N3+=1
#
            # if column == 5:
                # N4+=1
#
            # processedNuc=processedNuc+column +1
#

            break
        if column == 2:
            column1 = ValNow
        if column == 3:
            column2 = ValNow






        if column == 4:
            column3 = ValNow
            alleles=column1+column2+column3
            if unique_count(alleles)>2:
                Other+=1
                break


        if column == 5:
            column4 = ValNow
            alleles=column1+column2+column3+column4
            if unique_count(alleles)>2:
                Other+=1
                break

            #print column1+column2
            # if column4 == column1 and column4==column2 and column4 != column3:
                # AABA+=1
                #print alleles + " is AABA"
            # if column4 == column1 and column4!=column2 and column4 == column3:

                #print alleles + " is ABAA"
            if column4 == column1 and column4!=column2 and column4 != column3:
                ABBA+=1
                #print alleles + " is ABBA"

            # if column4 != column1 and column4==column2 and column4 == column3:

                #print alleles + " is BAAA"
            if column4 != column1 and column4==column2 and column4 != column3:
                BABA+=1
                #print alleles + " is BABA"
            # if column4 != column1 and column4!=column2 and column4 == column3:
                # BBAA+=1
                #print alleles + " is BBAA"
            # if column4 != column1 and column4!=column2 and column4 != column3:
                # BBBA+=1
    return (ABBA,BABA)


chrom ="1"
with open(fileName) as f:
    for line in f:
        row = line.split()
        if line1:
            line1=False

            continue


        numRows +=1



        # for column in range(len(row)):
            # chrom_change = chrom
            # chrom = row[0]
#
#
            # pos = int(float(row [1]))
            # ValNow = row[column]
            # if ValNow=="N":
                #print "This row has an N"
                # Other+=1
                # Ncount+=1
                # if column == 2:
                    # N1+=1
                # if column == 3:
                    # N2+=1
                # if column == 4:
                    # N3+=1
#
                # if column == 5:
                    # N4+=1
#
                # processedNuc=processedNuc+column +1
                # break
            # if column == 2:
                # column1 = ValNow
            # if column == 3:
                # column2 = ValNow
#
#




            # if column == 4:
                # column3 = ValNow
                # alleles=column1+column2+column3
                # if unique_count(alleles)>2:
                    # Other+=1
                    # break
#
#
            # if column == 5:
                # column4 = ValNow
                # alleles=column1+column2+column3+column4
                # if unique_count(alleles)>2:
                    # Other+=1
                    # break
#
                #print column1+column2
                # if column4 == column1 and column4==column2 and column4 != column3:
                    # AABA+=1
                    #print alleles + " is AABA"
                # if column4 == column1 and column4!=column2 and column4 == column3:

                    #print alleles + " is ABAA"
                #if column4 == column1 and column4!=column2 and column4 != column3:
                    #ABBA+=1
                    #print alleles + " is ABBA"

                # if column4 != column1 and column4==column2 and column4 == column3:

                    #print alleles + " is BAAA"
                #if column4 != column1 and column4==column2 and column4 != column3:
                    #BABA+=1
                    #print alleles + " is BABA"
                # if column4 != column1 and column4!=column2 and column4 == column3:
                    # BBAA+=1
                    #print alleles + " is BBAA"
                # if column4 != column1 and column4!=column2 and column4 != column3:
                    # BBBA+=1




            if chrom!=chrom_change:
                blockNum=1
                #print "the new bloc will start at position",start_pos
                block_range = str(start_pos)+"-"+str(prev_pos)
                (val,pval)=chi2_test(ABBA,BABA)
                D_stat = dstat(ABBA,BABA)
                D_cube = dcube(ABBA,BABA)
                line_toAppend = str(chrom_change)+"\t"+str(block_range)+"\t"+str(ABBA)+ "\t"+str(BABA)+"\t" + str(D_stat)+"\t"+str(D_cube)+"\t"+str(val)+"\t" +str(pval)+"\n"
                #print line_toAppend
                with open(outName, "a") as myfile:
                    myfile.write(line_toAppend)



                #print "******************\nThe chromosomejust changed from chromosome"+chrom_change+ "and position",prev_pos," to chromosome "+chrom+" and position ", pos," on the new chromosome\n************************"
                start_pos=pos
                ABBA=0
                BABA=0


                #print row
            #print row
            if pos/500 == blockNum:
                print "the current position is ",pos
                # print "the range is ",(blockNum -1)*500000 +1,"-",pos

                block_range = str(start_pos)+"-"+str(pos)
                start_pos = pos
                #block.append([chrom,block_range,ABBA,BABA])
                (val,pval)=chi2_test(ABBA,BABA)
                D_stat = dstat(ABBA,BABA)
                D_cube = dcube(ABBA,BABA)
                line_toAppend = str(chrom)+"\t"+str(block_range)+"\t" +str(ABBA)+ "\t"+str(BABA)+"\t" + str(D_stat)+"\t"+str(D_cube)+"\t"+str(val)+"\t" +str(pval)+"\n"
                print line_toAppend
                #print row[0],"\t",pos,"\n"

                #
                with open(outName, "a") as myfile:
                    myfile.write(line_toAppend)
#


                #print " there have been ",ABBA," ABBA and ",BABA," BABA"
                #print row
                blockNum+=1
                ABBA=0
                BABA=0
            prev_pos=pos

            # if chrom_change!=chrom and chrom_change!="":
                # print " the chromosome has changed from ",chrom_change, " to ",chrom
                # print "the new block range is ",(blockNum -1)*500000 +1,"-",pos
                # blockNum+=1
#
            #line = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"

# print "the current block is ",blockNum
# print "the block range is ",(blockNum -1)*500000 +1,"-",blockNum*500000
# print " there have been ",ABBA," ABBA and ",BABA," BABA"


#block.append([chrom,block_range,ABBA,BABA])
block_range = str(start_pos)+"-"+str(pos)
(val,pval)=chi2_test(ABBA,BABA)

line_toAppend = str(chrom)+"\t"+str(block_range)+"\t"+ str(ABBA)+ "\t"+str(BABA)+"\t"+str(val)+"\t" +str(pval)+"\n"
with open(outName, "a") as myfile:
    myfile.write(line_toAppend)


#
# with open(outName, "a") as myfile:
    # myfile.write(line_toAppend)
#

totNuc = 4*numRows
percenProcessed = float(processedNuc)/float(totNuc)*100

print "there were ",totNuc, " nucleotides to be processed"
print "we only had to process ", processedNuc
print "That means we only had to look at ", percenProcessed,"% of the nucleotides!"
#print "ABBA = ",ABBA
#print "BABA = ",BABA

#print abbaMatrix

            # if BABA == False and column2==column3:
