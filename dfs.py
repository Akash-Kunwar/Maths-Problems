from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,v,u):
        self.graph[v].append(u)
    def dfs(self,s):
        visited=[False]*len(self.graph)
        self.dfs_print(s,visited)
    def dfs_print(self,s,visited):
        visited[s]=True
        print(s)
        for i in self.graph[s]:
            if(visited[i]==False):
                self.dfs_print(i,visited)
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.dfs(2)