a=['']*26
sen=input().strip()
for i in range(len(sen)):
    if(sen[i].isupper()==True):
        temp=a[ord(sen[i])-ord('A')]
        temp+=sen[i]
        a[ord(sen[i])-ord('A')]=temp
    else:
        temp=a[ord(sen[i])-ord('a')]
        temp+=sen[i]
        a[ord(sen[i])-ord('a')]=temp

i=0
j=len(a)-1
s=''
# print(a)
# print(i,j)
while(i<j):
    if(a[i]==''):
        i+=1
    if(a[j]==''):
        j-=1
    if(a[i]!='' and a[j] !=''):
        if i==j:
            s+=a[i]
            i+=1
            j-=1
        else:
            s+=a[i]
            s+=a[j]
            i+=1
            j-=1

print(s)