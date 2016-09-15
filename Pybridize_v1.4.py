import sys
import collections

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue


def unique_count(thing):

    uniq_char_string=''.join(set(thing))
    uniq_char_count = len(uniq_char_string)
    return uniq_char_count

if "-i" in sys.argv:
    fileName = getOptionValue("-i")
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()

#
if "-p" in sys.argv:
    popString = getOptionValue("-p")
    if "P1" in sys.argv:
        pop1 =getOptionValue("P1")
    if "P2" in sys.argv:
        pop2 =getOptionValue("P2")
    if "P3" in sys.argv:
        pop3 =getOptionValue("P3")
    if "P4" in sys.argv:
        pop4 =getOptionValue("P4")
    if count_bool:
        fourPops = pop1 +' '+pop2+' '+pop3 + ' '+ pop4Inds
        for i in range(len(fourPops)):
            if len(i.split()) !=1:

                print " Please only choose one name per P1-P4"
                sys.exit


elif "-count" not in sys.argv:
  print "\nplease specify populations using -p\n"
  sys.exit()

count_bool=False
freq_bool=False
CountNames=""
P1Name=""
P2Name=""
P3Name=""
P4Name=""
P5Name=""

if "-count" in sys.argv:
    CountNames=getOptionValue("-count")
    if len(CountNames.split()) in (4 , 5):
        #print "FUCKKKKKKK"
        print len(CountNames.split())
        print CountNames.split()
        for i in range(len(CountNames.split())):
            if i ==0:
                P1Name=CountNames.split()[0]
            if i ==1:
                P2Name=CountNames.split()[1]
            if i ==2:
                P3Name=CountNames.split()[2]
            if i ==3:
                P4Name=CountNames.split()[3]
            if i ==4:
                P5Name=CountNames.split()[4]
        count_bool=True
    else:
        print len(CountNames.split())
        print CountNames.split()
        print 'please indicate the names of the four or five taxa to be analyzed using\n -count "taxa1 taxa2 taxa3 taxa4" \n as they appear in the datafile'
        sys.exit()




if "-freq" in sys.argv:
    try:
        taxa_num = getOptionValue("-freq")
    except:
        print "please indicate number of taxa using -freq <taxa number>\ncurrently only supports 4 taxa"
        sys.exit()
    if taxa_num=="4":
        print "we will proceed with frequency values of 4 taxa"
        freq_bool=True

    else:
        print "please indicate number of taxa using -freq <taxa number>\ncurrently only supports 4"
        sys.exit()
    # else:
        # print "Please indicate whether using counts or frequency as well as the taxa number using -count <taxa number> or -freq <taxa number>"

if "-w" in sys.argv:
    winSize = float(getOptionValue("-w"))
else:
    print "\nplease specify window size using -w <window size> \n"
    sys.exit()

ABBA=0
BABA=0
with open(fileName) as f:
    names = f.readline().strip()
    names = names.split()


#print pop1

#print pop2


if freq_bool or count_bool:

    pop1Tot=1
    pop2Tot=1
    pop1Inds={}
    pop2Inds={}
    pop3Tot=1
    pop4Tot=1
    pop3Inds={}
    pop4Inds={}


    pop1Members=0
    pop2Members=0
    pop3Members=0
    pop4Members=0
    pop1string=""
    pop2string=""
    pop3string=""
    pop4string=""
    pop1freq=0
    pop2freq=0
    pop3freq=0
    pop4freq=0
    pop1Alleles=""
    pop2Alleles=""
    pop3Alleles=""
    pop4Alleles=""


    for i in range(len(names)):
        #print names[i]
        #print i
        if count_bool:
            if names[i] == P1Name:
                P1Pos = i
            if names[i] == P2Name:
                P2Pos = i
            if names[i] == P3Name:
                P3Pos = i
            if names[i] == P4Name:
                P4Pos = i
            if names[i] == P5Name:
                P5Pos = i
        elif freq_bool:
            if names[i] in pop1:
                print "this is in pop1"
                pop1Inds[i]="pop1Ind"+str(pop1Tot)
                pop1Tot+=1
            if names[i] in pop2:
                print "this is in pop2"
                pop2Inds[i]="pop2Ind"+str(pop2Tot)
                pop2Tot+=1
            if names[i] in pop3:
                print "this is in pop3"
                pop3Inds[i]="pop3Ind"+str(pop3Tot)
                pop3Tot+=1
            if names[i] in pop4:
                print "this is in pop4"
                pop4Inds[i]="pop4Ind"+str(pop4Tot)
                pop4Tot+=1
        else:
            print count_bool
            print "one of those names wasn't in your file header"
            sys.exit()

# if count_bool:
    # for i in range(len(names)):


def Dcount(row):
    global P1Pos
    global P2Pos
    global P3Pos
    global P4Pos
    global P5Pos
    global ABBA
    global BABA
    P1Val=""
    P2Val=""
    P3Val=""
    P4Val=""
    p5Val=""




    for column in range(len(row)):
        ValNow=row[column]
        pos = row[1]
        if column in (P1Pos,P2Pos,P3Pos,P4Pos,P5Pos):
            if ValNow=="N":
                #print "there is an N position:"+pos
                break
            if column==P1Pos:
                P1Val=ValNow
            if column == P2Pos:
                P2Val=ValNow
                if P1Val == P2Val:
                    #print P1Val+P2Val+" are the same thing, neither ABBA or BABA position:"+pos
                    break
            if column == P3Pos:
                P3Val = ValNow
                alleles = P1Val+P2Val+P3Val
                if unique_count(alleles)!=2:
                    #print alleles+" will not be biallelic position:"+pos
                    break
            if column == P4Pos:
                P4Val=ValNow
                #print "OOOOOOOOOOOOO"
                alleles=P1Val+P2Val+P3Val+P4Val
                #print alleles
                if len(alleles)!=4:
                    print "***********************ALERT"
                    continue
                if unique_count(alleles)!=2:
                    #print "Definitely not biallelic"
                    #print alleles+ " is not biallelic"
                    break
                if P3Val==P4Val:
                    #print alleles+ " neither Abba or Baba position:"+pos
                    break
                if P2Val==P3Val:

                    #print alleles+" is ABBA"
                    ABBA +=1
                else:
                    #print alleles+' is BABA'
                    BABA+=1



            if column == P5Pos:
                P5Val = ValNow
        #return (ABBA,BABA)
    #print ABBA
    #print BABA
    return (ABBA,BABA)





def Dfreq(row):
    global pop1Members
    global pop2Members
    global pop3Members
    global pop4Members
    global pop1string
    global pop2string
    global pop3string
    global pop4string
    global pop1freq
    global pop2freq
    global pop3freq
    global pop4freq
    global pop1Alleles
    global pop2Alleles
    global pop3Alleles
    global pop4Alleles
    global ABBA
    global BABA




    for column in range(len(row)):

        ValNow=row[column]
        pos=row[1]
        if column in (pop1Inds, pop2Inds, pop3Inds, pop4Inds):
            if ValNow=="N":
                break
        # "**************************************"
        # if ValNow == "N":
            #print "Break for N"
            # break

        #print column
            #print "rope"
            #print column in pop1Inds
        if column in pop1Inds:
            pop1Members+=1
            pop1string= pop1string+ValNow
            if pop1Members ==pop1Tot-1:
                pop1Members=0
                pop1Alleles=pop1string
                pop1string=""


        if column in pop2Inds:
            pop2Members+=1
            pop2string=pop2string+ValNow
            if pop2Members== pop2Tot-1:
                pop2Members=0
                pop2Alleles=pop2string
                pop2string=""

        if column in pop3Inds:
            pop3Members+=1
            pop3string=pop3string+ValNow
            if pop3Members== pop3Tot-1:
                pop3Members=0
                pop3Alleles=pop3string
                pop3string=""

        if column in pop4Inds:
            pop4Members+=1
            pop4string=pop4string+ValNow
            if pop4Members== pop4Tot-1:
                pop4Members=0

                CombinedString= pop1Alleles+pop2Alleles+pop3Alleles+pop4string
                if unique_count(CombinedString)==2:
                    pop4Alleles=pop4string

                    majorAllele= GetMajorAllele(CombinedString)
                    #print majorAllele
                    #print AlleleFreq(pop1Alleles,majorAllele)
                    #print pop1Alleles+" 1a2 "+pop2Alleles+" 2b3 "+pop3Alleles+" 3c4 "+pop4string+" 4d "+pos
                    pop1freq=AlleleFreq(pop1Alleles,majorAllele)
                    pop2freq=AlleleFreq(pop2Alleles,majorAllele)
                    pop3freq=AlleleFreq(pop3Alleles,majorAllele)
                    pop4freq=AlleleFreq(pop4Alleles,majorAllele)
                    ABBA = (1-pop1freq)*pop2freq*pop3freq*(1-pop4freq)
                    #print ABBA

                    #print BABA
                    BABA = pop1freq*(1-pop2freq)*pop3freq*(1-pop4freq)
                pop4string=""

    return (ABBA,BABA)

#print pop1Inds
#print pop2Inds
print "*********************************************************************\n\n\n\n"
line1=True

ABBA = 0
BABA = 0
pos=0


majorAllele=""
def GetMajorAllele(string):
    letterdict=collections.Counter(string)


    allele1 = list(letterdict.values())[0]
    allele2 = list(letterdict.values())[1]
    if allele1> allele2:
        #majorAllele=allele1
        majorAlleleVal = list(letterdict.keys())[0]
        #minorAllele=allele2
    else:
        #majorAllele=allele2
        majorAlleleVal = list(letterdict.keys())[1]
        #minorAllele=allele1
    return majorAlleleVal


def AlleleFreq(string, majorAllele):
    letterdict = collections.Counter(string)
    allele_freq = float(letterdict.get(majorAllele,None))/len(string)
    return allele_freq



CandidatePos=""
#print 3 in pop1Inds
chrom="1"
blockNum=1
block_range=""
start_pos=1
prev_pos=1
with open(fileName) as f:

    for line in f:
        row = line.split()
        if line1:
            line1=False
            print "Continue for line 1"
            continue

        pop1Members=0

        chrom_change=chrom
        chrom = row[0]
        pos = int(float(row [1]))

        #print chrom +" "+chrom_change
        if count_bool:
            (ABBA,BABA)=Dcount(row)
        if freq_bool:
            (ABBA,BABA)=Dfreq(row)

        if chrom != chrom_change:
            blockNum=1
            block_range = str(start_pos) + "-" + str(prev_pos)
            if freq_bool:
                print Dfreq(row)
            elif count_bool:
                #print Dcount(row)
                #(ABBA,BABA)=Dcount(row)
                line_toAppend = str(chrom_change)+"\t"+str(block_range)+"\t"+str(ABBA)+ "\t"+str(BABA)
                print line_toAppend
                start_pos=pos
                ABBA=0
                BABA=0
        if pos/winSize == blockNum:
            #print "something"
            if freq_bool:
                print
            if count_bool:
                block_range = str(start_pos)+"-"+str(pos)
                start_pos = pos
                #(ABBA,BABA) = Dcount(row)
                line_toAppend=str(chrom)+"\t"+str(block_range)+"\t" +str(ABBA)+ "\t"+str(BABA)
                print line_toAppend
                blockNum+=1
                ABBA=0
                BABA=0
        prev_pos=pos


        #
        # if freq_bool:
            # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
#
#
            # print Dfreq(row)
        # elif count_bool:
            # print Dcount(row)
