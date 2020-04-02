test=int(input().strip())
for i in range(test):
    x=0
    y=0
    n=int(input().strip())
    path=list(input())
    temp=''
    for i in range(n):
        if path[i]=='L'  and (temp=='U' or temp=='D' or temp==''):
            x-=1
        elif path[i]=='R' and (temp=='U' or temp=='D' or temp==''):
            x+=1
        elif path[i]=='U' and (temp=='L' or temp=='R' or temp==''):
            y+=1
        elif path[i]=='D' and (temp=='L' or temp=='R' or temp==''):
            y+=1
        temp=path[i]
    # print(x,y)
        

