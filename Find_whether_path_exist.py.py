def ValidPath(mat,i,j,n,di,dj):
    if i<0 or j <0 or i> n-1 or j> n-1:
        return False
    elif mat[i][j]==0:
        return False
    elif i==di and j==dj:
        return True
    else:
        mat[i][j]=0
        return ValidPath(mat,i+1,j,n,di,dj) or ValidPath(mat,i,j+1,n,di,dj) or ValidPath(mat,i-1,j,n,di,dj) or ValidPath(mat,i,j-1,n,di,dj)
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    mat=[[0]*n for i in range(n)]
    temp=0
    ii=0
    jj=0
    di=0
    dj=0
    for i in range(n):
        for j in range(n):
            mat[i][j]=arr[temp]
            if mat[i][j]==1:
                ii=i
                jj=j
            if mat[i][j]==2:
                di=i
                dj=j
            temp+=1
    if ValidPath(mat,ii,jj,n,di,dj)==True:
        print(1)
    else:
        print(0)