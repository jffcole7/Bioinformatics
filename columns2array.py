#!/usr/bin/python

import csv
import sys



calls_table = []


def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue


if "-i" in sys.argv:
    fileName = getOptionValue("-i")
else:
    print "\nplease specify input file name using -i <file_name> \n"
    sys.exit()

with open(fileName) as f:
    reader = csv.reader(f, delimiter="\t")

    calls_table = list(reader)

print calls_table

#insert amazing loop here
