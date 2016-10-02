chrom=2
pos=28
P1=37
P2=36
P3=35
P4=33
P5=37
P6=36
P7=35
P8=32
P9=4


popNames = [chrom,pos,P1,P2,P3,P4,P5,P6,P7,P8,P9]

for popName in popNames:
   print popName
   print vars()[popName]
   print "\n"
