import random
a =''.join(random.choice('ATCG') for _ in range(random.randint(500,10000)))
#print a
count=0
print "chrom\tpos\tP1\tP2\tP3\tO"
chrom = 1
chrom_change=chrom
while count <5500:

    #if chrom !=chrom_change:
    count=count +1
    if random.randint(1,75)==random.randint(50,800):
        chrom_change=chrom
        chrom+=1
    if chrom_change!=chrom:
        count=1
        chrom_change=chrom




    print chrom,"\t",count,"\t"+random.choice('ATCGATCGN') +"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')
# print len(a)
# print "Will this show up on my github account?"
# print "I added this today"
