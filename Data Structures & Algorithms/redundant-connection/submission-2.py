class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(n+1))
        rank=[1]*(len(edges)+1)
        
        def find(i):
            root=i
            while parent[root]!=root:
                root=parent[root]
            
            while parent[i]!=root:
                parent[i],i=root,parent[i]
            return root

        def union(i,j):
            r1,r2=find(i),find(j)

            if rank[r1]>rank[r2]:
                parent[r2]=r1
                rank[r1]+=rank[r2]

            elif rank[r1]<=rank[r2]:
                parent[r1]=r2
                rank[r2]+=rank[r1]

        for edge in edges:
            if find(edge[1])==find(edge[0]):
                return edge
            union(edge[0],edge[1])
