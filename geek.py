from collections import defaultdict
class Graph:
    def __init__(self):
        self.count=0
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.count+=1
        print(count)
for _ in range(int(input())):
    g=Graph()
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(len(arr),2):
        u=arr[i]
        v=arr[i+1]
        print(u,v)
        g.addEdge(u,v)
    print(g.graph)
        
        
        