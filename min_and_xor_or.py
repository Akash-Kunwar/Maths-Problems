for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    m=999999
    arr.sort()
    for i in range(n-1):
        if(m>((arr[i]&arr[i+1])^(arr[i]|arr[i+1]))):
                m=(arr[i]&arr[i+1])^(arr[i]|arr[i+1])
    print(m)

    