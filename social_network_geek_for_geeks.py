for test in range(int(input())):
    n=int(input())
    mat=[ [999]*n for i in range(n)]
    path=list(map(int,input().split()))
    for i in range(len(path)):
        mat[i+1][path[i]-1]=1
    for i in range(n):
        for j in range(n):
            if i==j:
                mat[i][j]=0
    # print(mat)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j])
    # print(mat)

    for i in range(1,n):
        for j in range(n):
            if mat[i][j]!=999 and mat[i][j]!=0:
                print(i+1,j+1,mat[i][j],end=' ')
    print()
            