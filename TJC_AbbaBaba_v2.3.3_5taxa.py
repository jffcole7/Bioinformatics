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


    #
# if "-o" in sys.argv:
  # outName = getOptionValue("-o")
  #out = open(outName, "w")
# else:
  # print "\nplease specify output file name using -o <file_name> \n"
  # sys.exit()
#
# with open(outName,'wb') as out:
        # out.write("chrom\tblockRange\tABBA\tBABA\n")
#
#





numRows = 0
#totNuc =4*numRows
processedNuc =0

ABBA_bool = True
BABA_bool = True


AAAAA=0
AAABA=0
AABAA=0
AABBA=0
ABAAA=0
ABABA=0
ABBAA=0
ABBBA=0
BAAAA=0
BAABA=0
BABAA=0
BABBA=0
BBAAA=0
BBABA=0
BBBAA=0
BBBBA=0
def unique_count(thing):

    uniq_char_string=''.join(set(thing))
    uniq_char_count = len(uniq_char_string)
    return uniq_char_count



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
chrom = ""
pos = ""
#block=[]
blockNum =1
row =[]
#chrom_change=""

#print abbaMatrix
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






            if column == 4:
                column3 = ValNow

                alleles=column1+column2+column3
                if unique_count(alleles)>2:
                    #print alleles + " will not be biallalelic"#
                    break




            if column == 5:
                column4 = ValNow
                alleles=column1+column2+column3+column4
                if unique_count(alleles)>2:
                    #print alleles + " will not be biallalelic either"
                    break


            if column == 6:
                column5 = ValNow


                alleles=column1+column2+column3+column4+column5
                if unique_count(alleles)>2:
                    #print alleles + " will definitely not be biallalelic"
                    break

                if column5== column1 and column5 == column2 and column5 == column3 and  column5 == column4:
                    AAAAA+=1
                    #print column1+column2+column3+column4+column5 + " is AAAAA 1"

                if column5== column1 and column5 == column2 and column5 == column3 and  column5 != column4:
                    AAABA+=1
                    #print column1+column2+column3+column4+column5 + " is AAABA 2"
                if column5== column1 and column5 == column2 and column5 != column3 and  column5 == column4:
                    AABAA+=1
                    #print column1+column2+column3+column4+column5 + "is AABAA 3"
                if column5== column1 and column5 == column2 and column5 != column3 and  column5 != column4:
                    AABBA+=1
                    #print column1+column2+column3+column4+column5 + "is AABBA 4"



                if column5== column1 and column5 != column2 and column5 == column3 and  column5 == column4:
                    ABAAA+=1
                    #print column1+column2+column3+column4+column5 + " is ABAAA 5"
                if column5== column1 and column5 != column2 and column5 == column3 and  column5 != column4:
                    ABABA+=1
                    #print column1+column2+column3+column4+column5+ " is ABABA 6"
                if column5== column1 and column5 != column2 and column5 != column3 and  column5 == column4:
                    ABBAA+=1
                    #print column1+column2+column3+column4+column5 + " is ABBAA 7"
                if column5== column1 and column5 != column2 and column5 != column3 and  column5 != column4:
                    ABBBA+=1
                    #print column1+column2+column3+column4+column5+ " is ABBBA 8"




                if column5!= column1 and column5 == column2 and column5 == column3 and  column5 == column4:
                    BAAAA+=1
                    #print column1+column2+column3+column4+column5 + " is BAAAA 9"
                if column5!= column1 and column5 == column2 and column5 == column3 and  column5 != column4:
                    BAABA+=1
                    #print column1+column2+column3+column4+column5 + " is BAABA 10"
                if column5!= column1 and column5 == column2 and column5 != column3 and  column5 == column4:
                    BABAA+=1
                    #print column1+column2+column3+column4+column5 + " is BABAA 11"
                if column5!= column1 and column5 == column2 and column5 != column3 and  column5 != column4:
                    BABBA+=1
                    #print column1+column2+column3+column4+column5 + " is BABBA 12"




                if column5!= column1 and column5 != column2 and column5 == column3 and  column5 == column4:
                    BBAAA+=1
                    #print column1+column2+column3+column4+column5 + " is BBAAA 13"
                if column5!= column1 and column5 != column2 and column5 == column3 and  column5 != column4:
                    BBABA+=1
                    #print column1+column2+column3+column4+column5 + " is BBABA 14"
                if column5!= column1 and column5 != column2 and column5 != column3 and  column5 == column4:
                    BBBAA+=1
                    #print column1+column2+column3+column4+column5 + " is BBBAA 15"
                if column5!= column1 and column5 != column2 and column5 != column3 and  column5 != column4:
                    BBBBA+=1
                    #print column1+column2+column3+column4+column5 + " is BBBBA 16"











            #line = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"

            if chrom!=chrom_change:
                blockNum=1
                print "the new bloc will start at position",start_pos
                block_range = str(start_pos)+"-"+str(prev_pos)
                line_toAppend= str(chrom_change)+"\t" +str(block_range)+"\t"+str(AAAAA)+"\t"+ str(AAABA)+"\t"+ str(AABAA)+"\t"+ str(AABBA)+"\t"+ str(ABAAA)+"\t"+ str(ABABA)+"\t"+ str(ABBAA)+"\t"+ str(ABBBA)+"\t" + str(BAAAA) +"\t"+str(BAABA) +"\t"+ str(BABAA) +"\t"+str(BABBA) +"\t"+str(BBAAA) +"\t"+str(BBABA) +"\t"+str(BBBAA) +"\t"+str(BBBBA)+"\n"
                print line_toAppend



                print "******************\nThe chromosomejust changed from chromosome"+chrom_change+ "and position",prev_pos," to chromosome "+chrom+" and position ", pos," on the new chromosome\n************************"
                start_pos=pos
                AAAAA=0
                AAABA=0
                AABAA=0
                AABBA=0
                ABAAA=0
                ABABA=0
                ABBAA=0
                ABBBA=0
                BAAAA=0
                BAABA=0
                BABAA=0
                BABBA=0
                BBAAA=0
                BBABA=0
                BBBAA=0
                BBBBA=0
            prev_pos=pos
                #print row
            #print row
            if pos/500000 == blockNum:
                # print "the current block is ",blockNum
                # print "the range is ",(blockNum -1)*500000 +1,"-",pos

                block_range = str(start_pos)+"-"+str(pos)
                start_pos = pos
                #block.append([chrom,block_range,ABBA,BABA])
                #line_toAppend = str(chrom)+"\t"+str(block_range)+"\t"+str(ABBA)+"\t"+str(BABA)+"\n"
                line_toAppend= str(chrom)+"\t" +str(block_range)+"\t"+str(AAAAA)+"\t"+ str(AAABA)+"\t"+ str(AABAA)+"\t"+ str(AABBA)+"\t"+ str(ABAAA)+"\t"+ str(ABABA)+"\t"+ str(ABBAA)+"\t"+ str(ABBBA)+"\t" + str(BAAAA) +"\t"+str(BAABA) +"\t"+ str(BABAA) +"\t"+str(BABBA) +"\t"+str(BBAAA) +"\t"+str(BBABA) +"\t"+str(BBBAA) +"\t"+str(BBBBA)+"\n"

                print line_toAppend
                #print row[0],"\t",pos,"\n"

                #
                # with open(outName, "a") as myfile:
                    # myfile.write(line_toAppend)
#
                    #

                #print " there have been ",ABBA," ABBA and ",BABA," BABA"
                #print row
                blockNum+=1
                AAAAA=0
                AAABA=0
                AABAA=0
                AABBA=0
                ABAAA=0
                ABABA=0
                ABBAA=0
                ABBBA=0
                BAAAA=0
                BAABA=0
                BABAA=0
                BABBA=0
                BBAAA=0
                BBABA=0
                BBBAA=0
                BBBBA=0

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
line_toAppend= str(chrom)+"\t" +str(block_range)+"\t"+str(AAAAA)+"\t"+ str(AAABA)+"\t"+ str(AABAA)+"\t"+ str(AABBA)+"\t"+ str(ABAAA)+"\t"+ str(ABABA)+"\t"+ str(ABBAA)+"\t"+ str(ABBBA)+"\t" + str(BAAAA) +"\t"+str(BAABA) +"\t"+ str(BABAA) +"\t"+str(BABBA) +"\t"+str(BBAAA) +"\t"+str(BBABA) +"\t"+str(BBBAA) +"\t"+str(BBBBA)+"\n"


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
