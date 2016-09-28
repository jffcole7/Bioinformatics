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
if "-o" in sys.argv:
  outName = getOptionValue("-o")
  #out = open(outName, "w")
else:
  print "\nplease specify output file name using -o <file_name> \n"
  sys.exit()

with open(outName,'wb') as out:
        out.write("chrom\tblockRange\tABBA\tBABA\n")



























numRows = 0
#totNuc =4*numRows
processedNuc =0

ABBA_bool = True
BABA_bool = True
ABBA=0
BABA=0
ValNow=""
column1="same"
column2="stillthis"
column3="pleasebedifferent"
column4="donotshowup"
line1=True
abbaMatrix=[]
#abbaMatrix.append(['chrom','pos','ABBA'])
chrom = ""
pos = ""
block=[]
blockNum =1
chrom_change=""

print abbaMatrix
with open(fileName) as f:
    for line in f:
        row = line.split()
        if line1:
            line1=False

            continue


        numRows +=1







        for column in range(len(row)):
            chrom_change = chrom
            chrom = row[0]


            pos = int(float(row [1]))
            ValNow = row[column]
            if ValNow=="N":
                #print "This row has an N"

                processedNuc=processedNuc+column +1
                break
            if column == 2:
                column1 = ValNow
            if column == 3:
                column2 = ValNow
                if column2 == column1:

                    #print column1+column2 +" are the same thing"
                    processedNuc=processedNuc+2
                    break



            if column == 4:
                column3 = ValNow
                if column3 != column1 and column3 != column2:
                    #print column1+column2+column3+"is not biallelic"
                    processedNuc = processedNuc+3
                    break

                if column3 == column2 and column3 != column1:
                    BABA_bool = False

                else:
                    ABBA_bool = False
            if column == 5:
                column4 = ValNow
                if column4==column3:
                    #print column1+column2+column3+column4+" You will not be goingto space today "
                    break
                    processedNuc=processedNuc+4
                if column4!=column1 and column4!=column2:
                    #print column1+column2+column3+column4+" There is an extra letter in here "
                    processedNuc=processedNuc+4
                    break

                if column4 == column1:
                    #print column1+column2+column3+column4+" This is ABBA!!!!! chrom ="+chrom+" pos =",pos
                    abbaMatrix.append([chrom,pos,1])

                    ABBA+=1
                    processedNuc=processedNuc+4
                else:
                    #print column1+column2+column3+column4+" This is BABA!!!!! chrom="+chrom+" pos =",pos
                    abbaMatrix.append([chrom,pos,0])

                    BABA+=1
                    processedNuc=processedNuc+4
            #line = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"
            if pos/500 == blockNum:
                print "the current block is ",blockNum
                print "the range is ",(blockNum -1)*500 +1,"-",pos
                block_range = str((blockNum -1)*500 +1)+"-"+str(pos)
                block.append([chrom,block_range,ABBA,BABA])
                line = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"
                with open(outName, "a") as myfile:
                    myfile.write(line)

                #print " there have been ",ABBA," ABBA and ",BABA," BABA"
#
                blockNum+=1
                ABBA=0
                BABA=0
            # if chrom_change!=chrom and chrom_change!="":
                # print " the chromosome has changed from ",chrom_change, " to ",chrom
                # print "the new block range is ",(blockNum -1)*500 +1,"-",pos
                # blockNum+=1
#
            #line = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"

print "the current block is ",blockNum
print "the block range is ",(blockNum -1)*500 +1,"-",blockNum*500
print " there have been ",ABBA," ABBA and ",BABA," BABA"
block.append([chrom,block_range,ABBA,BABA])
line = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"
with open(outName, "a") as myfile:
    myfile.write(line)
print block

totNuc = 4*numRows
percenProcessed = float(processedNuc)/float(totNuc)

print "there were ",totNuc, " to be processed"
print "we only had to process ", processedNuc
print "we only looked at ", percenProcessed
print "ABBA = ",ABBA
print "BABA = ",BABA

#print abbaMatrix

            # if BABA == False and column2==column3: