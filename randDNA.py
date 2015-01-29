import random
a =''.join(random.choice('ATCG') for _ in range(random.randint(500,10000)))
print a
print len(a)
