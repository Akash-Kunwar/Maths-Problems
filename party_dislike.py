# EFFECTIVE METHOD

n=int(input())
d={}
for i in range(10):
    arr=list(map(int,input().split()))
    d[arr[0]]=arr[1:]
count=0
for i in d.keys():
    arr=d[i]
    for j in arr:
        count+=1
        if(j in d.keys() and i in d[j]):
            d[j].remove(i)
print((n*(n-1)/2)-count)


