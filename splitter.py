def get_intv(string,borders = "()",inc = False):
  if len(borders) != 2:
    print "WARNING: borders must contain two characters"
  starts = []
  ends = []
  output = []
  for x in range(len(string)):
    if string[x] == borders[0]:
      starts.append(x)
    if string[x] == borders[1]:
      ends.append(x+1)
  if len(starts) <= len(ends):
    for n in range(len(starts)):
      if inc:
        output.append(string[starts[n]:ends[n]])
      else:
        output.append(string[starts[n]+1:ends[n]-1])
  else:
    for n in range(len(ends)):
      if inc:
        output.append(string[starts[n]:ends[n]])
      else:
        output.append(string[starts[n]+1:ends[n]-1])
  return output
popNames=[]
indName=[]
popStrings = '"alpha[alpha1,alpha2];beta[beta1,beta2];gamma[gamma1,gamma2];delta[delta1,delta2]"'
#print popstring
#print popstring.strip("\"").split(";")[0]
for popstring in popStrings.strip("\"").split(";"):
    currentPop= popStrings.split("[")[0]
    popNames.append(currentPop)
    #vars()[currentPop] = get_intv(popstring,"[]")[0].split(",")
    #for indNamein vars()[currentPop]:
print popNames    
