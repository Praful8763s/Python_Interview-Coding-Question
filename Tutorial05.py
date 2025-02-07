class GraphDFS: 
    def __init__(self): 
        self.adjList = {} 
 
    def add_edge(self, v, w): 
        if v not in self.adjList: 
            self.adjList[v] = [] 
        if w not in self.adjList: 
            self.adjList[w] = [] 
        self.adjList[v].append(w) 
 
    def dfs(self, start): 
        visited = set() 
        self._dfs_rec(start, visited) 
 
    def _dfs_rec(self, vertex, visited): 
        if vertex not in visited: 
            visited.add(vertex) 
            print(vertex, end=" ") 
            for neighbor in self.adjList.get(vertex, []): 
                self._dfs_rec(neighbor, visited) 
 
if __name__ == "__main__": 
    g = GraphDFS() 
    g.add_edge(1, 2) 
    g.add_edge(1, 3) 
    g.add_edge(2, 4) 
    g.add_edge(3, 4) 
    g.add_edge(4, 5) 
 
    g.dfs(1)