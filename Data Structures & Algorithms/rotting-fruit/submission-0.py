class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dist=[[-1]*cols for _ in range (rows)]
        q=deque()
        sources=[]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                    dist[i][j]=0
                elif not grid[i][j]:
                    dist[i][j]=0

        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and dist[nr][nc]==-1 and grid[nr][nc]==1:
                    dist[nr][nc]=dist[r][c]+1
                    q.append((nr,nc))
        flat=[d for row in dist for d in row]
        if -1 in flat:
            return -1
        return max(flat)
