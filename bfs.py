from collections import defaultdict 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,v,u):
        self.graph[v].append(u)
    def bfs(self,s):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(s)
        visited[s]=True
        while(len(queue)!=0):
            vertex=queue.pop(0)
            print(vertex,'')
            for i in self.graph[vertex]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
            
            
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.bfs(2)