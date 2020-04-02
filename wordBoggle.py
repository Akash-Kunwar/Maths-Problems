def words(mat,maxlen,dic,s,ans,i,j,sol):
    if i<0 or j<0 or i>n-1 or j>m-1:
        return
    elif sol[i][j]==1:
        return 
    elif s in dic:
        ans.append(s)
        dic.remove(s)
        return

    elif len(s)>=maxlen:
        return
    
    else:
        sol[i][j]=1
        words(mat,maxlen,dic,s+mat[i][j],ans,i-1,j-1,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i-1,j,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i-1,j+1,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i,j-1,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i,j+1,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i+1,j-1,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i+1,j,sol)
        words(mat,maxlen,dic,s+mat[i][j],ans,i+1,j+1,sol)
        sol[i][j]=0
        


for test in range(int(input())):
    lenDic=int(input())
    dic=input().split()
    maxlen=0
    for i in dic:
       if len(i)>maxlen:
          maxlen=len(i)
      
    n,m=map(int,input().split())
    temp=input().split()
    mat=[['']*m for i in range(n)]
    k=0
    for i in range(n):
       for j in range(m):
          mat[i][j]=temp[k]
          k+=1
    ans=[]
    sol=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            words(mat,maxlen,dic,'',ans,i,j,sol)

    print(ans)
