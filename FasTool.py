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
header=""
switch =0
DoOnce=True
seqType=""
<<<<<<< HEAD
Ccount=0
text =""
Ccount = 0
def CysCount(sequence):
    global Ccount
    text = sequence
    for i in range(len(text)):
        if text[i] == "C":
            Ccount+=1
    Ccount = Ccount/float(len(sequence))*1000
    return Ccount
    Ccount = 0


=======
def cysCount(sequence):
    cysCount=0
    for i in range(len(sequence)):
        if sequence[i]=="C":
            cysCount+=1
    return cysCount

def cysMotif(sequence):
    NumCys = cysCount(sequence)
    BeginCysGapCount=False
    NumCysChange=False
    CysGap=-1
    motif=""
    for i in range(len(sequence)):
        if BeginCysGapCount:
            CysGap+=1
        if sequence[i]=="C":
            #print "C"
            motif+="C-"
            BeginCysGapCount = True
            NumCys = NumCys-1
            NumCysChange=True
        if NumCysChange:
            #print CysGap
            motif+=str(CysGap)+"-"
            CysGap=-1
            NumCysChange=False
    motif+="C"
    motif= motif[5:len(motif)]
    return motif
if "-cys" in sys.argv:
    CysMotifOnly=True
else:
    CysMotifOnly=False
<<<<<<< HEAD
    # a comment 
=======
>>>>>>> 363b46bbac46b61859fe02016687a22e3f9bb237
>>>>>>> c3933112e77984ec4ca877ed18ff6948cf6a2fdc

#2for line in range(len(fasta_file)):c
with open(fileName) as f:

    for line in f:
        line = line.strip()

        header_bool=False
        sequence_bool = False

        if ">" in line:
            if switch == 0:
                header1= line

                seq_length = 0
                sequence=""
                switch = 1
            elif switch == 1:
                if DoOnce:

                    firstNuc = sequence[0]
                    LastNuc = sequence[-1]
                    if firstNuc=="M" and LastNuc=="*":
                        seqType= "complete"
                    else:
                        seqType="incomplete"
                    #first sequence
                    if CysMotifOnly:
                        if cysCount(sequence)>3:

                            print cysCount(sequence),cysMotif(sequence), header1
                    else:

<<<<<<< HEAD
                    #print header1,"len:"+str(seq_length),"type:"+seqType
                    #print sequence
                    print CysCount(sequence)
=======
                        print header1,"len:"+str(seq_length),"type:"+seqType,
                        print sequence
>>>>>>> 363b46bbac46b61859fe02016687a22e3f9bb237
                    DoOnce=False

                try:
                    firstNuc = sequence[0]
                    LastNuc = sequence[-1]
                    if firstNuc=="M" and LastNuc=="*":
                        seqType= "complete"
                    else:
                        seqType="incomplete"
                    #middle sequence
                    if CysMotifOnly:
                        if cysCount(sequence)>3:

<<<<<<< HEAD
                    #print old_header,"len:"+str(seq_length),"type:"+seqType
                    #print sequence
                    print CysCount(sequence)
=======
                            print cysCount(sequence),cysMotif(sequence),header
                    else:
                        print old_header,"len:"+str(seq_length),"type:"+seqType,"cysteine:"+cysCount(sequence)
                        print sequence
>>>>>>> 363b46bbac46b61859fe02016687a22e3f9bb237
                except:
                    0

                header = line
                old_header=header

                seq_length = 0
                sequence=""
        else:
            seq_length+=len(line)
            sequence+=line

firstNuc = sequence[0]
#print firstNuc

LastNuc = sequence[-1]
#print LastNuc
if firstNuc=="M" and LastNuc=="*":
    seqType= "complete"
else:
    seqType="incomplete"
#last sequence
if CysMotifOnly:
    if cysCount(sequence)>3:

        print cysCount(sequence),cysMotif(sequence),header
else:
    print header,"len:"+str(seq_length),"type:"+seqType
    print sequence
