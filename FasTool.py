#fasta_file = [">a","CGGCATGCTAGCGCATGC","CATGCTAGCTGACTGACGTACGTACG",">b","AGGCATGCTAGCGCATGC","ACGTGCGATCGTAGCGATGATGCACG","ACAGCTAGCGTCATGCA",">c","AGGCATGCTAGCGCATGC"]
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


#for line in range(len(fasta_file)):
with open(fileName) as f:

    for line in f:



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
                    print header1,"len:"+str(seq_length)
                    print sequence
                    DoOnce=False

                try:
                    print old_header,"len:"+str(seq_length)
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


print header,"len:"+str(seq_length)
print sequence
