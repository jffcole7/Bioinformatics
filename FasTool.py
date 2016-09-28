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

                    print header1,"len:"+str(seq_length),"type:"+seqType
                    print sequence
                    DoOnce=False

                try:
                    firstNuc = sequence[0]
                    LastNuc = sequence[-1]
                    if firstNuc=="M" and LastNuc=="*":
                        seqType= "complete"
                    else:
                        seqType="incomplete"

                    print old_header,"len:"+str(seq_length),"type:"+seqType
                    print sequence
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

print header,"len:"+str(seq_length),"type:"+seqType
print sequence
