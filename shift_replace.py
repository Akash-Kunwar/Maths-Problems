n=int(input())
arr=list(map(int,input().split()))
# print(arr)
test=int(input())
# print(test)
for i in range(test):
    posele=input().split()
    pos=int(posele[0])
    ele=int(posele[1])
    arr[pos-1]=ele
    count=0
    print(arr)
    temp=[0]*n
    for j in range(n):
        temp[i]=arr[i]
    if(temp[0]!=temp[1]-1):
        count+=1
        temp.insert(n-1,temp.pop(0))
    for j in range(n):
        if(temp[j]!=j+1):
            count+=1
    print(count)



