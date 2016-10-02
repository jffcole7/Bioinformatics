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
      pop1Inds={}
      pop1 =getOptionValue("P1")

  if "P2" in sys.argv:
        pop2 =getOptionValue("P2")
  if "P3" in sys.argv:
        pop3 =getOptionValue("P3")
  if "P4" in sys.argv:
        pop4 =getOptionValue("P4")


else:
  print "\nplease specify populations using -p\n"
  sys.exit()
#
count_bool=False
freq_bool=False
if "-count" or "-freq" in sys.argv():
    if "-count" in sys.argv:
        taxa_num = getOptionValue("-count")
        if taxa_num==4:
            print "We will proceed with count values of 4 taxa"
            count_bool =True
        elif taxa_num ==5:
            print " We will proceed with count values of 5 taxa, doing D-FOIL"
            count_bool = True
        else:
            print "please indicate number of taxa using -count <taxa number> \ncurrently only supports 4 and 5"
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
    else:
        print "Please indicate whether using counts or frequency as well as the taxa number using -count <taxa number> or -freq <taxa number>"
        sys.exit()


ABBA=0
BABA=0
with open(fileName) as f:
    names = f.readline().strip()
    names = names.split()


#print pop1

#print pop2


if freq_bool:

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
#


    for i in range(len(names)):
        #print names[i]
        #print i
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

print pop1Inds
print pop2Inds
print "*********************************************************************\n\n\n\n"
line1=True

ABBA = 0
BABA = 0
pos=0

#
# pop1Members=0
# pop1string=""
# pop2string=""
# pop2Members=0
# pop3string=""
# pop3Members=0
# pop4string=""
# pop4Members=0
# pop1freq=0
# pop2freq=0
# pop3freq=0
# pop4freq=0
#
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

    # allele1 = list(letterdict.values())[0]
    # allele2 = list(letterdict.values())[1]
    # if allele1> allele2:
        # majorAllele=allele1
        # majorAlleleVal = list(letterdict.keys())[0]
        # minorAllele=allele2
    # else:
        # majorAllele=allele2
        # majorAlleleVal = list(letterdict.keys())[1]
        # minorAllele=allele1
#
    # allele_freq= float(majorAllele)/ (float(majorAllele) +float(minorAllele))
#

    return allele_freq



    # ABBA = (1-pop1freq)*pop2freq*pop3freq*(1-pop4freq)
    # BABA = pop1freq*(1-pop2freq)*pop3freq*(1-pop4freq)
    # return (ABBA,BABA)
#
CandidatePos=""
print 3 in pop1Inds
with open(fileName) as f:

    for line in f:
        row = line.split()
        if line1:
            line1=False
            print "Continue for line 1"
            continue

        pop1Members=0
    #
        if freq_bool:


            print Dfreq(row)



                                        #
