for i in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    d={}
    count=0
    for i in range(len(arr)):
        if arr[i]  in d.keys():
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    for i in d.keys():
        if k-i in d.keys():
            if i==k-i:
                count+=(d[i]*(d[i]-1))//2
            else:
                count+=d[i]*d[k-i]
            d[i]=0
    
            
    print(count)