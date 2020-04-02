# form the largest even number from the string
# input:'abcd1234'
# output:4312


s=input()
t=[0]*10
a=[]
for i in range(len(s)):
    if(s[i]>='0' and s[i]<='9'):
        if(t[ord(s[i])-ord('0')]==0):
            a.append(s[i])
            t[ord(s[i])-ord('0')]=1


# print(a)
a.sort()
a.reverse()
count=0
# print(a)
if(int(a[-1])%2!=0):
    for i in range(len(a)-2,-1,-1):
        if(int(a[i])%2==0):
            rep=a[i]
            a.remove(a[i])
            a.insert(len(a),rep)
            count=1
            break
else:
    print(''.join(a))
if(count==0):
    print(-1)
else:
    print(''.join(a))