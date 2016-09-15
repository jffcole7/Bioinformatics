import random
a =''.join(random.choice('ATCG') for _ in range(random.randint(500,10000)))
#print a
count=0
print "chrom\tpos\tP1\tP2\tP3\tP4\tP5\tP6\tP7\tP8\tP9"
chrom = 1

count=0
chrom = 1
chrom_change=chrom
while count <2300:

    #if chrom !=chrom_change:
    count=count +1
    if random.randint(1,75)==random.randint(50,400):
        chrom_change=chrom
        chrom+=1
    if chrom_change!=chrom:
        count=1
        chrom_change=chrom
    #print chrom,"\t",count,"\t"+random.choice('ATCGATCG') +"\t"+random.choice('ATCGATCG') +"\t"+random.choice('ATCGATCG') +"\t"+random.choice('ATCGATCG')+"\t"+random.choice('ATCGATCG') +"\t"+random.choice('ATCGATCG')+"\t"+ random.choice('ATCGATCG') +"\t"+ random.choice('ATCGATCG') +"\t"+random.choice('ATCGATCG')+"\t"+random.choice('ATCG')
    print chrom,"\t",count,"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')+"\t"+random.choice('ACTGACTGN')
