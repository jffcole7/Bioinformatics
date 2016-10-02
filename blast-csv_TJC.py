#! /usr/bin/env python
import sys
import csv
import blastparser

# get the filename as the first argument on the command line
filename = sys.argv[1]

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-o" in sys.argv:
  outName = getOptionValue("-o")
else:
  print "\nplease specify output file name using -o <file_name> \n"
  sys.exit()

# open it for reading
fp = open(filename)

# send output as comma-separated values to stdout
output = csv.writer(sys.stdout)

# parse BLAST records
for record in blastparser.parse_fp(fp):
    for hit in record:
        for match in hit.matches:
            # output each match as a separate row
            row = record.query_name + "\t" + hit.subject_name + "\t" + match.score + "\t" + match.expect
            output.writerow(row)
            with open(outName, "a") as myfile:
                myfile.write(row)
