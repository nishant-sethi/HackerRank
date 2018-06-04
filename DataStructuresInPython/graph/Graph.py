'''
Created on Jun 4, 2018

@author: nishant.sethi
'''
import collections
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
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
            self.gdict[vertex] = []
            
            
    # Add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
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
        while queue:
            vertex = queue.popleft()
            self.marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
    
    def marked(self,n):
        print(n)
    

