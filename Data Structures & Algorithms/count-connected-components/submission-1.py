from collections import deque 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited=[]
        queue=deque([])
        counter=0
        
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if i not in visited:
                counter+=1
                queue.append(i)    
                while queue:
                    v=queue.popleft()
                    if v not in visited:
                        visited.append(v)
                        for el in adj[v]:
                            queue.append(el)   
        return counter