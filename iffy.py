import sys
def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-o" in sys.argv:
  outName = getOptionValue("-o")
  #out = open(outName, "w")
else:
  print "\nplease specify output file name using -o <file_name> \n"
  sys.exit()

with open(outName, "a") as myfile:
    myfile.write("iffy")
