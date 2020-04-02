# array->2 6 3 5 8 9
# largest fibonocii series->[2, 3, 5, 8]

a=list(map(int,input().split()))
min1=min(a)
a.remove(min1)
min2=min(a)
a.remove(min2)
s=''
s+=str(min1)
s+=str(min2)
while(True):
    if(a.count(min1+min2)>0):
        sfind=min1+min2
        a.remove(sfind)
        s+=str(sfind)
        min1=min2
        min2=sfind
    else:
        break
print(list(map(int,s)))
        

