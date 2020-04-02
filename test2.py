test=int(input())
for i in range(test):
    n=int(input())
    arr=list(map(int,input().split()))
    ind=arr.index(max(arr))
    ele=max(arr)
    mid=n//2
    if ind <= mid and ele in arr[mid:mid+ind+1]:
        print(0)
    else:
        print(ind)
    
