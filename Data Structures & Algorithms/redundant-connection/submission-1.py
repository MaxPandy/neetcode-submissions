class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(n+1))
        
        def find(i):
            root=i
            while parent[root]!=root:
                root=parent[root]
            
            while parent[i]!=root:
                parent[i],i=root,parent[i]
            return root

        def union(i,j):
            r1,r2=find(i),find(j)
            if r1!=r2:
                parent[r1]=r2

        for edge in edges:
            if find(edge[1])==find(edge[0]):
                return edge
            union(edge[0],edge[1])
