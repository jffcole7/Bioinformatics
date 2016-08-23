import random
a =''.join(random.choice('ATCG') for _ in range(random.randint(500,10000)))
#print a
count=0
print "chrom\tpos\tP1\tP2\tP3\tO"
chrom = 1
while count <499:
    count=count +1
    if count%10==0:
        chrom+=1



    print chrom,"\t",count,"\t"+random.choice('ATCGATCGN') +"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')
# print len(a)
# print "Will this show up on my github account?"
# print "I added this today"
