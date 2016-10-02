pop1Inds=[8,3,5]
pop2Inds=[2,4,6]
pop3Inds=[9,8,7]
pop4Inds=[6,4,10]
ValNow=""
pop1Length=len(pop1Inds)
pop2Length=len(pop2Inds)
pop3Length=len(pop3Inds)
pop4Length=len(pop4Inds)
pop1Tot =0
pop2Tot =0
pop3Tot =0
pop4Tot =0
pop1=""
pop2=""
pop3=""
pop4=""
row = ["chrom","pos","A","N","C","G","T","G","C","A","C"]
for i in range(len(row)):
    #break
    ValNow=row[i]
    if i in pop1Inds:
        pop1Tot+=1

        pop1=pop1+ValNow
    if i in pop2Inds:
        pop2Tot+=1

        pop2=pop2 + ValNow
    if i in pop3Inds:
        pop3Tot+=1

        pop3=pop3+ValNow
    if i in pop4Inds:
        pop4Tot+=1

        pop4=pop4+ValNow
apple="app epp ekke"
print pop1
print pop2
print pop3
print pop4
print len(apple.split())
