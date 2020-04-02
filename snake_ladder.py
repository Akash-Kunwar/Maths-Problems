def bfs(board,visited):
    q=[]
    q.append([1,0])
    while(len(q)!=0):
        cur=q.pop(0)
        curV=cur[0]
        curD=cur[1]
        # print(curV)
        if curV==30:
            break
        else:
            for i in range(curV+1,curV+7):
                if i<=30 and visited[i]==0:
                    visited[i]=1
                    if board[i]!=0:
                        q.append([board[i],curD+1])
                    else:
                        q.append([i,curD+1])
        # print(q)
        
    return curD 
                    
for test in range(int(input())):
    board=[0]*31
    nl=int(input())
    l=list(map(int,input().split()))
    for i in range(0,nl+1,2):
        board[l[i]]=l[i+1]
    # print(board)
    visited=[0]*31
    visited[0]=1
    print(bfs(board,visited))