string=input()
i=len(string)-1
j=len(string)//2
while(True):
    if(string[i]==string[j]):
        i-=1
        j-=1
print(string[j:len(string)]
