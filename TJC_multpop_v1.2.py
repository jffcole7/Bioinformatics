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


with open(fileName) as f:
    names = f.readline().strip()
    names = names.split()


print pop1

print pop2

pop1Tot=1
pop2Tot=1
pop1Inds={}
pop2Inds={}
pop3Tot=1
pop4Tot=1
pop3Inds={}
pop4Inds={}

for i in range(len(names)):
    print names[i]
    print i
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
line1=True

ABBA = 0
BABA = 0


pop1Members=0
pop1string=""
pop2string=""
pop2Members=0
pop3string=""
pop3Members=0
pop4string=""
pop4Members=0
pop1freq=0
pop2freq=0
pop3freq=0
pop4freq=0



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


def Dfreq(row):
    pop1Members=0
    pop1string=""
    pop2string=""
    pop2Members=0
    pop3string=""
    pop3Members=0
    pop4string=""
    pop4Members=0
    pop1freq=0
    pop2freq=0
    pop3freq=0
    pop4freq=0

    for column in range(len(row)):

        if column in pop1Inds:
            pop1Members+=1
            if row[column]=="N":
                break
            pop1string= pop1string+row[column]
            if pop1Members ==pop1Tot-1:
                pop1Members=0
                #print pop1string
                if unique_count(pop1string)==2:
                    pop1freq = AlleleFreq(pop1string)
                    pop1string=""
                else:
                    pop1string=""
                    break


        if column in pop2Inds:
            pop2Members+=1
            if crow[column]=="N":
                break
            pop2string=pop2string+row[column]
            if pop2Members== pop2Tot-1:
                pop2Members=0
                #print pop2string+"pop2"
                if unique_count(pop2string)==2:
                    pop2freq=AlleleFreq(pop2string)
                    pop2string=""
                else:
                    pop2string=""
                    break

        if column in pop3Inds:
            pop3Members+=1
            pop3string=pop3string+row[column]
            if pop3Members== pop3Tot-1:
                pop3Members=0
                #print pop3string+"pop3"
                if unique_count(pop3string)==2:
                    pop3freq= AlleleFreq(pop3string)
                    pop3string=""
                else:
                    pop3string=""
                    break

        if column in pop4Inds:
            pop4Members+=1
            pop4string=pop4string+row[column]
            if pop4Members== pop4Tot-1:
                pop4Members=0
                #print pop4string+"pop4"
                if unique_count(pop4string)==2:
                    pop4freq= AlleleFreq(pop4string)
                    pop4string=""
                else:
                    pop4string=""
                    break

    ABBA = (1-pop1freq)*pop2freq*pop3freq*(1-pop4freq)
    BABA = pop1freq*(1-pop2freq)*pop3freq*(1-pop4freq)
    return (ABBA,BABA)
with open(fileName) as f:

    for line in f:
        row = line.split()
        if line1:
            line1=False

            continue

            #
        # for column in range(len(row)):
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



        (ABBA,BABA)=Dfreq(row)
        print ABBA," is ABBA, but ",BABA," is BABA"
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
