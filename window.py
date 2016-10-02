b = [1,10,300,400,499,500,501,515,600,700,999,1000,1001,1300]
winNum = 1
block = []
sum = 0

for i in range(len(b)):
    #print b[i]
    #print  b[i]/500 ,b[i]
    print b[i], "/500 is", b[i]/500
    print "winNum is ", winNum
    if b[i]/500 <winNum:
        #print b[i], " things ",winNum
        sum+=b[i]


    if b[i]/500 == winNum:
        sum+=b[i]
        print "the current window is ", winNum
        print "the sum is ", sum
        block.append([winNum,sum])
        winNum+=1


        sum=0
block.append([winNum,sum])
print "the current window is ", winNum
print "the sum is ", sum
print block
