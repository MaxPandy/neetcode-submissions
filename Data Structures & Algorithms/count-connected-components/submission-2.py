from collections import deque 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited=[False]*n
        queue=deque([])
        counter=0
        
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if not visited[i]:
                counter+=1
                visited[i]=True
                queue.append(i)  

                while queue:
                    node=queue.popleft()
                    for el in adj[node]:
                        if not visited[el]:
                            visited[el]=True
                            queue.append(el)   
        return counter