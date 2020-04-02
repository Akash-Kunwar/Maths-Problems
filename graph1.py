from collections import defaultdict
class Graph:
    def __init__(self,croad,clib,n):
        self.road=croad
        self.lib=clib
        self.total=0
        self.V=n
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,v):
        # print(self.graph[v])
        visited=[False]*self.V
        for i in self.graph[v]:
            if visited[i]==False:
                self.total+=self.lib
                print(self.total)
                self.dfs_utils(i,visited)
    def dfs_utils(self,v,visited):
        print(v)
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.total+=self.road
                print(self.total)
                self.dfs_utils(i,visited)

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return n*c_lib
    else:
        g=Graph(n,c_road,c_lib)
        for city in cities:
            g.addEdge(city[0]-1,city[1]-1)
        g.dfs(0)
        return g.total
roadsAndLibraries(5,6,1,[[1,2],[1,3],[1,4]])