numbers = "0 0 0 0 0 1 0 0 1 2 3 0 0 1 2 3 4 5 0 0 0 0 1 0 0 0 1 2 0 0 0"
num_array = numbers.split()
prev_value = "nothing"

import sys

def getOptionValue(option):
    optionPos = [i for i, j in enumerate(sys.argv) if j == option][0]
    optionValue = sys.argv[optionPos + 1]
    return optionValue

if "-i" in sys.argv:
    inputFile = getOptionValue("-i")
else:
    print "no"
    sys.exit()


with open(inputFile) as f:
    for line in f:
        current_value = f[line]
        if prev_value==current_value:

            print prev_value,current_value," are the same: 0"
        if prev_value>current_value:
            if prev_value=="nothing":
                print current_value, " is smaller than ", prev_value, " : 0"
            else:

                print current_value, " is smaller than ", prev_value, " :",prev_value
        prev_value= current_value


        #
        # row = line.split()
        #go = row[1].split(",")
        # for i in range(len(go)):
#
            #
# for i in range(len(num_array)):
    #print num_array[i]
    #if i !=0:
#
    #    prev_value = current_value
#
    # current_value = num_array[i]
    # if prev_value==current_value:
#
        # print prev_value,current_value," are the same: 0"
    # if prev_value>current_value:
        # if prev_value=="nothing":
            # print current_value, " is smaller than ", prev_value, " : 0"
        # else:
#
            # print current_value, " is smaller than ", prev_value, " :",prev_value
    # prev_value= current_value
