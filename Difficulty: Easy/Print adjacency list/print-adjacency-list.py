
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        adj = [[] for _ in range(V + 1)] 
        for u, v in edges:
            adj[u].append(v)  
            adj[v].append(u)  
    
        return adj  
        