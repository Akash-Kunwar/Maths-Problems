# array->1 1 2 1 1 3 4 5 6 8 9
# no. of deletions allowed->3
# minimum distict elements->5

a=list(map(int,input().split()))
temp=int(input())
arr=[0]*10
count=0
for i in a:
    if(arr[ord(str(i))-ord('0')]==0):
        arr[ord(str(i))-ord('0')]=1
        count+=1
    else:
        arr[ord(str(i))-ord('0')]+=1
# print(arr,count)
arr.sort()
i=0
# print(arr)
while(i<len(arr) and temp>0):
    if(arr[i]!=0):
        # print(arr[i],i,temp)
        c=temp
        temp-=arr[i]
        if c>=arr[i]:
            arr[i]=0
        else:
            arr[i]=arr[i]-c
        if arr[i]==0:
            count-=1
    i+=1
print(count)
print(arr)

