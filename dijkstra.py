class Graph(): 
    #constructor
    def __init__(self, vertices):
        self.distArray = [0 for i in range(vertices)]
        self.vistSet = [0 for i in range(vertices)]
        self.V = vertices
        self.INF = 1000000
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
  
    def printSolution(self, distArray): 
        print ("Node \tDistance from 0")
        for i in range(self.V): 
            print (i, "\t", distArray[i])
  
    #A utility function to find the vertex with minimum distance value, from 
	# the set of vertices not yet included in shortest path tree 
    def minDistance(self, distArray, vistSet): 
  
        # Initilaize minimum distArrayance for next node
        min = self.INF
  
        # Search not nearest vertex not in the  
        # unvisited nodes
        for v in range(self.V): 
            if distArray[v] < min and vistSet[v] == False: 
                min = distArray[v] 
                min_index = v 
  
        return min_index
        
    def dijkstra(self, srcNode):
        for i in range(self.V):
          #initialise the distArrayances to infinity first
          self.distArray[i] = self.INF
          #set the visited nodes set to false for each node
          self.vistSet[i] = False
        #initialise the first distArrayance to 0
        self.distArray[srcNode] = 0
        for i in range(self.V): 
  
            # Pick the minimum distArrayance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to srcNode in first iteration 
            u = self.minDistance(self.distArray, self.vistSet) 
  
            # Put the minimum distArrayance vertex in the  
            # visited nodes set
            self.vistSet[u] = True
  
             # Update dist[v] only if is not in sptSet, there is an edge from 
            # u to v, and total weight of path from src to  v through u is 
            # smaller than current value of dist[v]
            for v in range(self.V): 
                if self.graph[u][v] > 0 and self.vistSet[v] == False and self.distArray[v] > self.distArray[u] + self.graph[u][v]: 
                        self.distArray[v] = self.distArray[u] + self.graph[u][v] 
  
        self.printSolution(self.distArray)
#Display our vertices
ourGraph = Graph(7) 
ourGraph.graph = [[0, 2, 6, 0, 0, 0, 0], 
        [2, 0, 0, 5, 0, 0, 0], 
        [6, 6, 0, 8, 0, 0, 0], 
        [0, 0, 8, 0, 10, 15, 0], 
        [0, 0, 0, 10, 0, 6, 2], 
        [0, 0, 0, 15, 6, 0, 6], 
        [0, 0, 0, 0, 2, 6, 0],
        ]; 
  
ourGraph.dijkstra(0);