a=list(map(int,input().split()))
count=0
s=0
t=''
for i in a:
    if i==5 or count==1:
        t+=str(i)
        count=1
    else:
        s+=i
    if(i==8):
        count=0
print(t,s)
print(int(t)+s)

