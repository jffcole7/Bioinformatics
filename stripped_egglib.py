import sys

import egglib




def AlignByGroupNumber(align,groupNumber):
  newAlign = align.slice(0,0)
  for seqNumber in range(len(align)):
    if align[seqNumber][2] == groupNumber:
      newAlign.addSequences([align[seqNumber]])
  return newAlign

def unique(things):
  output = list(set(things))
  output.sort()
  return output



def colFreqs(align, columnNumber):
  bases = align.column(columnNumber)
  Acount = float(bases.count("A"))
  Ccount = float(bases.count("C"))
  Gcount = float(bases.count("G"))
  Tcount = float(bases.count("T"))
  total = Acount + Ccount + Gcount + Tcount
  if total > 0:
    output = {}
    output["A"] = Acount/total
    output["C"] = Ccount/total
    output["G"] = Gcount/total
    output["T"] = Tcount/total
  else:
    output = {"A":"NA", "C":"NA", "G":"NA", "T":"NA"}
  return output






def ABBABABA(align, P1, P2, P3, P4, P3a = None, P3b = None):
  p1Align = AlignByGroupNumber(align,P1)
  p2Align = AlignByGroupNumber(align,P2)
  p3Align = AlignByGroupNumber(align,P3)
  p4Align = AlignByGroupNumber(align,P4)
  if P3a == None or P3b == None:
    P3Half = len(P3Align)/2
    P3aAlign = P3Align.slice(0,P3Half)
    P3bAlign = P3Align.slice(P3Half,len(P3Align))
  else:
    p3aAlign = AlignByGroupNumber(align,P3a)
    p3bAlign = AlignByGroupNumber(align,P3b)
  ABBAsum = 0.0
  BABAsum = 0.0
  maxABBAsumG = 0.0
  maxBABAsumG = 0.0
  maxABBAsumHom = 0.0
  maxBABAsumHom = 0.0
  maxABBAsumD = 0.0
  maxBABAsumD = 0.0
  #get derived frequencies for all biallelic siites
  for i in align.polymorphism(minimumExploitableData = 0)["siteIndices"]:
    #skip this site if not biallelic
    bases = [base for base in align.column(i) if base != "N"]
    alleles = unique(bases)
    if len(alleles) != 2: continue
    #get derived state
    #if the outgroup is fixed, then that is the ancestral state - otherwise the anc state is the most common allele overall
    p4Alleles = unique([base for base in p4Align.column(i) if base != "N"])
    if len(p4Alleles) == 1:
      derived = [a for a in alleles if a != p4Alleles[0]][0]
    else:
      derived = [a for a in alleles if a != mostCommon(bases)[0]][0]
    # get frequencies for wach pop
    p1Freq = colFreqs(p1Align, i)[derived]
    p2Freq = colFreqs(p2Align, i)[derived]
    p3Freq = colFreqs(p3Align, i)[derived]
    p4Freq = colFreqs(p4Align, i)[derived]
    p3aFreq = colFreqs(p3aAlign, i)[derived]
    p3bFreq = colFreqs(p3bAlign, i)[derived]
    # get weigtings for ABBAs and BABAs
    try: # this was added to ignore crashes when there is missing data for a population at a site - we just ignore these sites
      ABBAsum += (1 - p1Freq) * p2Freq * p3Freq * (1 - p4Freq)
      BABAsum += p1Freq * (1 - p2Freq) * p3Freq * (1 - p4Freq)
      maxABBAsumG += (1 - p1Freq) * p3aFreq * p3bFreq * (1 - p4Freq)
      maxBABAsumG += p1Freq * (1 - p3aFreq) * p3bFreq * (1 - p4Freq)
      maxABBAsumHom += (1 - p1Freq) * p3Freq * p3Freq * (1 - p4Freq)
      maxBABAsumHom += p1Freq * (1 - p3Freq) * p3Freq * (1 - p4Freq)
      if p3Freq >= p2Freq:
        maxABBAsumD += (1 - p1Freq) * p3Freq * p3Freq * (1 - p4Freq)
        maxBABAsumD += p1Freq * (1 - p3Freq) * p3Freq * (1 - p4Freq)
      else:
        maxABBAsumD += (1 - p1Freq) * p2Freq * p2Freq * (1 - p4Freq)
        maxBABAsumD += p1Freq * (1 - p2Freq) * p2Freq * (1 - p4Freq)
    except:
      continue
      ###########################################################
      ########################################
      ##########################
  #calculate D, f and fb
  output = {}
  try:
    output["D"] = (ABBAsum - BABAsum) / (ABBAsum + BABAsum)
  except:
    output["D"] = "NA"
  try:
    output["fG"] = (ABBAsum - BABAsum) / (maxABBAsumG - maxBABAsumG)
  except:
    output["fG"] = "NA"
  try:
    output["fhom"] = (ABBAsum - BABAsum) / (maxABBAsumHom - maxBABAsumHom)
  except:
    output["fhom"] = "NA"
  try:
    output["fd"] = (ABBAsum - BABAsum) / (maxABBAsumD - maxBABAsumD)
  except:
    output["fd"] = "NA"
  output["ABBA"] = ABBAsum
  output["BABA"] = BABAsum

  return output

if "--minimumExploitableData" in sys.argv:
  minExD = float(getOptionValue("--minimumExploitableData"))
  print "minimumExploitableData =", minExD
else:
  minExD = 0
