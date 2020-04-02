def gcd(a,b):
    while(a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

arr=list(map(int,input().split()))
x=arr[0]
y=arr[1]
p=arr[2]
q=arr[3]

b1=p*y
b2=q*x
gcd=gcd(b1,b2)
b1=b1//gcd
b2=b2//gcd
b3=(x*b1+y*b2)//(p+q)
tb1=b1
tb2=b2
while(True):
    if (b3==0 or ((x*b1+y*b2)%(p+q))!=0):
        b1+=tb1
        b2+=tb2
        b3=(x*b1+y*b2)//(p+q)
    else:
        break

    
print(b1,b2,b3)
