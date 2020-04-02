import math
testcases=int(input())
test=0
while(test<testcases):
    n=int(input())
    count=0
    till=math.pow(2,n)
    i=0
    while(i<till):
        s=bin(i)[2:]
        if s.find('111')==-1:
            count+=1
        i+=1
    print(count%100000007)
    test+=1