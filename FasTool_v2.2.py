import itertools
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
else:
    print "\nplease specify output file name using -o <file_name> \n"
    sys.exit()

subset_bool=False
cysMotif_bool=False

if "-id" in sys.argv:
    wanted_file = getOptionValue("-id") # Input header id file to subset
    wanted = []
    with open(wanted_file) as f:
        for line in f:
            line = line.strip()
            if line != "":
                wanted.append(line)
    subset_bool =True
elif "-doCysMotif" in sys.argv:
    cysMotif_bool=True
else:
    print "either indicate to do subset or print cys motif"
    sys.exit()






def isheader(line):
    return line[0] == '>'


def cysCount(sequence):
    cysCount = 0
    for i in range(len(sequence)):
        if sequence[i] == "C":
            cysCount += 1
    return cysCount


def cysMotif(sequence):
    NumCys = cysCount(sequence)
    BeginCysGapCount = False
    NumCysChange = False
    CysGap = -1
    motif = ""
    for i in range(len(sequence)):
        if BeginCysGapCount:
            CysGap += 1
        if sequence[i] == "C":
            # print "C"
            motif += "C-"
            BeginCysGapCount = True
            NumCys = NumCys - 1
            NumCysChange = True
        if NumCysChange:
            # print CysGap
            motif += str(CysGap) + "-"
            CysGap = -1
            NumCysChange = False
    motif += "C"
    motif = motif[5:len(motif)]
    return motif

ensembl_id=""
def aspairs(file):

    for header, group in itertools.groupby(f, isheader):
        if header:
            line = group.next()
            ensembl_id = line
            print ensembl_id
            #ensembl_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield ensembl_id, sequence
            # print sequence
            if cysMotif_bool:
                if cysCount(sequence) > 3:
                    with open(outName, "a") as out:
                        line_toAppend = ensembl_id + "\t" + \
                            str(cysCount(sequence)) + "\t" + \
                            cysMotif(sequence) + "\t" + str(len(sequence)) + "\n"
                        out.write(line_toAppend)
            elif subset_bool:
                for id in range(len(wanted)):
                    if wanted[id] in ensembl_id:
                        with open(outName,"a") as out:
                            out.write(ensembl_id)
                        with open(outName,"a") as out:
                            out.write(sequence)



                    # print line_toAppend
if cysMotif_bool:
    with open(outName, "wb") as out:
        out.write("id\tCysCount\tCysMotif\tSeqLength\n")
with open(fileName) as f:
    d = dict(aspairs(f))
