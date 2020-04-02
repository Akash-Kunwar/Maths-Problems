def getDecision(m,n):
    pre=[]
    ans=[]
    while(m!=n):
        if m*2 >n//2:
            if m-1 in pre:
                m=m*2
                ans.append("overflow")
                pre.append(m*2)
            else:
                m=m-1
                ans.append("eat")
                pre.append(m-1)
        else:
            m=m*2
            ans.append("overflow")
            pre.append(m*2)
    return ans
print(getDecision(1,9))