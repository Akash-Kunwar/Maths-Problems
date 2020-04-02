def printPowerSet(fuel,set_size,f): 
    pow_set_size = 2**set_size 
    counter = 0; 
    j = 0; 
    count=0
    for counter in range(0, pow_set_size): 
        total=0
        for j in range(0, set_size):   
            if((counter & (1 << j)) > 0): 
                total+=fuel[j]
        if total==f:
            print('Yes')
            return 0
    return -1

    
for i in range(int(input())):
    arr=list(map(int,input().split()))[1:]
    f=int(input())
    k=int(input())
    fuel=[]
    for i in range(len(arr)):
        if(arr[i]<=k):
            fuel.append(arr[i])
    fuel.sort()
    if len(fuel)==0:
        print('No')
    elif fuel[0]>f:
        print('No')
    else:
        if printPowerSet(fuel,len(fuel),f)==-1:
            print('No')
                
                
        
        

