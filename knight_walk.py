def valid(i,j):
    if i>0 and i<n+1 and j>0 and j<n+1 and visited[i][j]==0:
        return True 
    return False
def bfs(mat,visited,ii,ij,fi,fj):
    q=[]
    q.append([ii,ij,0])
    visited[ii][ij]=1
        
    while(len(q)!=0):
        # print(q)
        thispos=q.pop(0)
        ti=thispos[0]
        tj=thispos[1]
        dist=thispos[2]
        
        if ti==fi and tj==fj:
            return dist
        if valid(ti+2,tj-1):
            q.append([ti+2,tj-1,dist+1])
            visited[ti+2][tj-1]=1
        
        if valid(ti+1,tj-2):
            q.append([ti+1,tj-2,dist+1])
            visited[ti+1][tj-2]=1
        
        if valid(ti-1,tj-2):
            q.append([ti-1,tj-2,dist+1])
            visited[ti-1][tj-2]=1
        
        if valid(ti-2,tj-1):
            q.append([ti-2,tj-1,dist+1])
            visited[ti-2][tj-1]=1
        
        if valid(ti-2,tj+1):
            visited[ti-2][tj+1]=1
        
            q.append([ti-2,tj+1,dist+1])
        if valid(ti-1,tj+2):
            visited[ti-1][tj+2]=1
        
            q.append([ti-1,tj+2,dist+1])
        if valid(ti+1,tj+2):
            visited[ti+1][tj+2]=1
        
            q.append([ti+1,tj+2,dist+1])
        if valid(ti+2,tj+1):
            visited[ti+2][tj+1]=1
        
            q.append([ti+2,tj+1,dist+1])
        
        
        
        
for i in range(int(input())):
    n=int(input())
    ii,ij=map(int,input().split())
    fi,fj=map(int,input().split())
    mat=[[0]*(n+1) for i in range(n+1)]
    visited=[[0]*(n+1) for i in range(n+1)]
    print(bfs(mat,visited,ii,ij,fi,fj))
    