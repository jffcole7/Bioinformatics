import random
a =''.join(random.choice('ATCG') for _ in range(random.randint(500,10000)))
#print a
count=0
print "P1"+"\t"+"P2"+"\t"+"P3"+"\t"+"O"
while count <10:

    print random.choice('ATCGATCGN') +"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')+"\t"+random.choice('ATCGATCGN')
    count=count +1
# print len(a)
# print "Will this show up on my github account?"
# print "I added this today"
