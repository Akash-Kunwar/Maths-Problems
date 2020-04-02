def count(mat,c,i,j,n,m):
    if i<0 or j<0  or i>n-1 or j>m-1:
        return 0
    elif  mat[i][j]==0:
        return 0
    else:
        mat[i][j]=0
        c=1
        c+=count(mat,c,i-1,j-1,n,m)
        c+=count(mat,c,i+1,j+1,n,m)
        c+=count(mat,c,i+1,j,n,m)
        c+=count(mat,c,i,j+1,n,m)
        c+=count(mat,c,i-1,j,n,m)
        c+=count(mat,c,i,j-1,n,m)
        c+=count(mat,c,i+1,j-1,n,m)
        c+=count(mat,c,i-1,j+1,n,m)
    return c

for test in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    mat=[[0]*m for i in range(n)]
    sol=[[0]*m for i in range(n)]
    temp=0
    for i in range(n):
        for j in range(m):
            mat[i][j]=arr[temp]
            temp+=1
    maxcount=0
    ct=[]
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                maxcount=max(maxcount,count(mat,0,i,j,n,m))
    print(maxcount)