'''
Created on Aug 19, 2018

@author: nishant.sethi
'''
import collections
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())


    #Display Edges
    def edges(self):
        return self.findedges()
    
    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex, vertex} not in edgename:
                    edgename.append({vertex, next_vertex})
        return edgename
    
    # Add the vertex as a key
    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict.update({vertex:[]})
            
            
    # Add the new edge
    def AddEdge(self, edge):
        #edge = set(edge)
        (vertex1, vertex2) = edge
        if vertex1 in self.gdict:
            if vertex2 not in self.gdict[vertex1]:
                self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]
            
    # Check for the visisted and unvisited nodes
    def dfs(self,graph,start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for nxt in (graph[start] - visited):
            self.dfs(graph, nxt, visited) 
        return visited
    
    def bfs(self,graph, startnode):
        # Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        visited=[]
        while queue:
            vertex = queue.popleft()
            self.marked(vertex)
            visited.append(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
    def marked(self,n):
        print(n)
        
    def printGraph(self):
        x=self.gdict
        print(sorted(x.items(),key=lambda x:x[0]))

    # finds shortest path between 2 nodes of a graph using BFS
    def bfs_shortest_path(self,graph, start, goal):
        # keep track of explored nodes
        explored = []
        # keep track of all the paths to be checked
        queue = [[start]]
     
        # return path if start is goal
        if start == goal:
            return "That was easy! Start = goal"
     
        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is goal
                    if neighbour == goal:
                        return new_path
     
                # mark node as explored
                explored.append(node)
     
        # in case there's no path between the 2 nodes
        return "So sorry, but a connecting path doesn't exist :("
       
q=int(input())
for i in range(q):
    g=Graph()
    results=''
    nodes,edges=map(int,input().split())
    for i in range(nodes):
        g.addVertex(i+1)
    for i in range(edges):
        u,v=map(int,input().split())
        g.AddEdge((u,v))
        g.AddEdge((v,u))
    s=int(input())
    #print(g.printGraph())
    for i in range(1,nodes+1):
        if i!=s:
            #print(s," ",i)
            result=g.bfs_shortest_path(g.gdict, i,s)
            if len(result)==48:
                #print(-1,end=" ")
                results+=str(-1)+" "
                #print(i," ",s," ",result)
            else:
                #print((len(result)-1)*6,end=" ")
                results+=str((len(result)-1)*6)+" "
                #print(i," ",s," ",result)
    print(results)