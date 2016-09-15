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


def AlleleFreq(string):
    letterdict = collections.Counter(string)


    allele1 = list(letterdict.values())[0]
    allele2 = list(letterdict.values())[1]
    if allele1> allele2:
        majorAllele=allele1
        minorAllele=allele2
    else:
        majorAllele=allele2
        minorAllele=allele1

    allele_freq= float(majorAllele)/ (float(majorAllele) +float(minorAllele))
    return allele_freq


# def Dfreq(columnValue,columnNumber):
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
#
    # if columnNumber in pop1Inds:
        # pop1Members+=1
#

        #if columnValue=="N":
        #    break
#
            #
        # pop1string= pop1string+columnValue
        # if pop1Members ==pop1Tot-1:
            # pop1Members=0
            #print pop1string
            # if unique_count(pop1string)==2:
                # pop1freq = AlleleFreq(pop1string)
                # pop1string=""
            # else:
                # pop1string=""
                # break
#
#
    # if columnNumber in pop2Inds:
        # pop2Members+=1
        #
        #if columnValue=="N":
        #    break

            #
        # pop2string=pop2string+columnValue
        # if pop2Members== pop2Tot-1:
            # pop2Members=0
            #print pop2string+"pop2"
            # if unique_count(pop2string)==2:
                # pop2freq=AlleleFreq(pop2string)
                # pop2string=""
            # else:
                # pop2string=""
                # break
#
    # if columnNumber in pop3Inds:
        # pop3Members+=1
        # pop3string=pop3string+columnValue
        # if pop3Members== pop3Tot-1:
            # pop3Members=0
            #print pop3string+"pop3"
            # if unique_count(pop3string)==2:
                # pop3freq= AlleleFreq(pop3string)
                # pop3string=""
            # else:
                # pop3string=""
                # break
#
    # if columnNumber in pop4Inds:
        # pop4Members+=1
        # pop4string=pop4string+columnValue
        # if pop4Members== pop4Tot-1:
            # pop4Members=0
            #print pop4string+"pop4"
            # if unique_count(pop4string)==2:
                # pop4freq= AlleleFreq(pop4string)
                # pop4string=""
            # else:
                # pop4string=""
                # break
#
    # ABBA = (1-pop1freq)*pop2freq*pop3freq*(1-pop4freq)
    # BABA = pop1freq*(1-pop2freq)*pop3freq*(1-pop4freq)
    # return (ABBA,BABA)
#
CandidatePos=0
print 3 in pop1Inds
with open(fileName) as f:

    for line in f:
        row = line.split()
        if line1:
            line1=False
            print "Continue for line 1"
            continue

            #
        for column in range(len(row)):
            ValNow=row[column]
            pos=row[1]
            if ValNow == "N":
                #print "Break for N"
                break

            #print column
            if freq_bool:
                #print "rope"
                #print column in pop1Inds
                if column in pop1Inds:
                    pop1Members+=1
                    #print "pop1 found"

                    #
                    # if ValNow=="N":
                        # break


                    pop1string= pop1string+ValNow
                    if pop1Members ==pop1Tot-1:
                        #print "Check"
                        pop1Members=0
                        #print pop1string
                        pop1Alleles=pop1string
                        pop1string=""
                        if unique_count(pop1Alleles)==2:
                            pop1freq = AlleleFreq(pop1Alleles)
                            #pop1Alleles = pop1string
                            #print "pop1 "+pop1Alleles+" at position "+pos
                            CandidatePos = pos

                            #pop1string=""
                        else:
                            #print "break for pop1 nonBiallelic "+pop1string

                            #pop1string=""
                            break

                    #print "Continue away from pop1"
                    #continue


                if column in pop2Inds:
                    pop2Members+=1

                    # if ValNow=="N":
                        # break
            #

                    pop2string=pop2string+ValNow
                    if pop2Members== pop2Tot-1:
                        pop2Members=0
                        #print pop2string+"pop2"
                        pop2Alleles=pop2string
                        pop2string=""
                        if CandidatePos==pos and unique_count(pop2Alleles)==2 :
                            #CandidatePos=pos
                            #if unique_count(pop2string)==2:
                            #pop2freq=AlleleFreq(pop2string)

                            CombinedString=pop2Alleles+pop1Alleles
                            if unique_count(CombinedString)!=2:
                                break
                                #pop2Alleles = pop2string

                                    #print "pop1 "+pop1Alleles+" at position "+CandidatePos
                                    #print"pop2 "+ pop2Alleles+" at position "+pos
                                    #pop2string=""
                                #else:
                                    #pop2string=""
                                    #break
                            #else:
                                #pop2string=""
                                #print "break pop2"
                                #break
                        #pop2string=""
                    #print "continue pop2"
                    #continue

                if column in pop3Inds:
                    pop3Members+=1
                    pop3string=pop3string+ValNow
                    if pop3Members== pop3Tot-1:
                        pop3Members=0
                        #print pop3string+"pop3"
                        if unique_count(pop3string)==2:
                            pop3freq= AlleleFreq(pop3string)
                            pop3Alleles=pop3string
                            if CandidatePos==pos:
                                CombinedString=pop1Alleles+pop2Alleles+pop3Alleles
                                #if unique_count(CombinedString)==2:

                                    #print "pop1 "+ pop1Alleles+" at position "+CandidatePos
                                    #print "pop2 "+pop2Alleles+" at position "+CandidatePos
                                    #print "pop3 "+ pop3Alleles+" at position "+pos

                                pop3string=""
                        else:
                            pop3string=""
                            #print "break pop3"
                            break
                    #print "continue pop3"
                    #continue

                if column in pop4Inds:
                    pop4Members+=1
                    pop4string=pop4string+ValNow
                    if pop4Members== pop4Tot-1:
                        pop4Members=0
                        #print pop4string+"pop4"
                        if unique_count(pop4string)==2:
                            pop4freq= AlleleFreq(pop4string)
                            pop4Alleles = pop4string
                            if CandidatePos==pos:
                                CombinedString= pop1Alleles+pop2Alleles+pop3Alleles+pop4Alleles
                                if unique_count(CombinedString)==2:
                                    print "pop1 "+ pop1Alleles+" at position "+CandidatePos
                                    print "pop2 "+pop2Alleles+" at position "+CandidatePos
                                    print "pop3 "+ pop3Alleles+" at position "+CandidatePos
                                    print "pop4 "+pop4Alleles+ " at position "+pos


                            #print pop4Alleles+" at position "+pos
                            pop4string=""
                        else:
                            pop4string=""
                            #print "break pop4"
                            break
                    else:
                        #print "continue pop4 "
                        continue





        #print "position is "+pos
        CombinedString = pop1Alleles+pop2Alleles+pop3Alleles+pop4Alleles
        if unique_count(CombinedString)==2:
            ABBA = (1-pop1freq)*pop2freq*pop3freq*(1-pop4freq)
            BABA = pop1freq*(1-pop2freq)*pop3freq*(1-pop4freq)


            #
            # print pop1Alleles
            # print pop2Alleles
            # print pop3Alleles
            # print pop4Alleles
            # print ABBA," is ABBA and BABA is ",BABA
#
    #print BABA
            # if column in pop1Inds:
                # pop1Members+=1
                # pop1string= pop1string+row[column]
                # if pop1Members ==pop1Tot-1:
                    # pop1Members=0
                    #print pop1string
                    # if unique_count(pop1string)==2:
                        # 1
                        # pop1freq = AlleleFreq(pop1string)
                    # pop1string=""
            # if column in pop2Inds:
                # pop2Members+=1
                # pop2string=pop2string+row[column]
                # if pop2Members== pop2Tot-1:
                    # pop2Members=0
                    #print pop2string+"pop2"
                    # if unique_count(pop2string)==2:
                        # 1
                        # pop2freq=AlleleFreq(pop2string)
                    # pop2string=""
            # if column in pop3Inds:
                # pop3Members+=1
                # pop3string=pop3string+row[column]
#
#
                # if pop3Members== pop3Tot-1:
                    # pop3Members=0
                    #print pop3string+"pop3"
                    # if unique_count(pop3string)==2:
                        # pop3freq= AlleleFreq(pop3string)
                    # pop3string=""
            # if column in pop4Inds:
                # pop4Members+=1
                # pop4string=pop4string+row[column]
#
#
                # if pop4Members== pop4Tot-1:
                    # pop4Members=0
                    #print pop4string+"pop4"
                    # if unique_count(pop4string)==2:
                        # pop4freq= AlleleFreq(pop4string)
                    # pop4string=""
#



        #(ABBA,BABA)=Dfreq(row)
        #print ABBA," is ABBA, but ",BABA," is BABA"
        #print BABA, " is BABA"

        #ABBA = (1-pop1freq)*pop2freq*pop3freq*(1-pop4freq)
        #BABA = pop1freq*(1-pop2freq)*pop3freq*(1-pop4freq)
        #print "ABBA is ",ABBA



            # if column == pop1Inds["pop1Ind1"]:
                # pop1Ind1 = column[row]


#


#
# pops = []
#for each population, store the name and individual names
# for popData in popString.strip("\"").split(";"):
  # currentPop = popData.split("[")[0]
  # pops.append(currentPop)
  #vars()[currentPop + "Inds"] = get_intv(popData,"[]")[0].split(",")
  # print currentPop
#


  # for ind in vars()[currentPop + "Inds"]:
    # if ind not in names:
      # print ind, "not found in header line."
      # sys.exit()
#
