st1=input().strip(' ')
l=len(set(st1))
t=int(input())
for i in range(t):
    st2=input()
    if(len(set(st1)|set(st2))==l):
        print('Yes')
    else:
        print('No')