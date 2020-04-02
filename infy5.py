# longest substring with unique charcters
# Input:ABCDAkkBccdDD
# Output:ABCD

s=input()
l=len(s)
unique=''
for i in range(len(s)):
    # count=0
    check=s[0:i+1]
    temp=s[l-1-i:l+1]
    # print(check)
    if(len(check)==len(set(check))):
        if(len(unique)<len(check)):
            unique=check
    if(len(temp)==len(set(temp))):
        if(len(unique)<len(temp)):
            unique=temp
    
print(unique)