#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
class Graph:
    def __init__(self,n,croad,clib):
        self.road=croad
        self.lib=clib
        self.total=0
        self.V=n
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[v].append(u)
        self.graph[u].append(v)
    def dfs(self,v):
        # print(self.graph)
        visited=[False]*self.V
        for i in range(self.V):
            if visited[i]==False:
                # print('lib',i)
                self.total+=self.lib
                self.dfs_utils(i,visited)
                
    def dfs_utils(self,v,visited):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.total+=self.road
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

   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
