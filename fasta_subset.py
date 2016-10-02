import sys
from Bio import SeqIO

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue
if "-fasta" in sys.argv:
    fasta_file = getOptionValue("-fasta") # Input fasta file
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()

if "-id" in sys.argv:
    wanted_file = getOptionValue("-id") # Input fasta file
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()

if "-out" in sys.argv:
    result_file = getOptionValue("-out") # Input fasta file
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()


wanted = []
with open(wanted_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            wanted.append(line)
#print wanted

            #
            # print "this line was added"
        # else:



fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        #print wanted[id] +" "+ seq.id
        for id in range(len(wanted)):


            #print wanted[id]+" " +seq.id
            if wanted[id] in seq.id:
                SeqIO.write([seq], f, "fasta")



    # for seq in fasta_sequences:
        # print wanted[id] +" "+ seq.id
        #print wanted[id]+seq.id


        # if wanted[id] in seq.id:
            # print seq

#
# with open(result_file, "w") as f:
    #
            #
    # for seq in fasta_sequences:
        # if seq.id in wanted:
            # SeqIO.write([seq], f, "fasta")
        # else:
                #
            #
