class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n+1))
        components=n
        def find(i):
            root=i
            while parent[root]!=root:
                root=parent[root]
            while parent[i]!=root:
                parent[i],i=root,parent[i]
            return root
        def union(i,j):
            r_i=find(i)
            r_j=find(j)
            parent[r_i]=r_j

        for edge in edges:
            e1=find(edge[0])
            e2=find(edge[1])
            if e1!=e2:
                union(e1,e2)
                components-=1
        return components