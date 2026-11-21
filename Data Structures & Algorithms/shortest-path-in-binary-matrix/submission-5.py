from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions = [(di, dj) for di, dj in product((-1, 0, 1), repeat=2) if (di, dj) != (0, 0)]
        row=len(grid)
        col=len(grid[0])
        dest=(row-1,col-1)

        if grid[0][0] or grid[row-1][col-1]:
            return -1

        visited=set()
        dq=deque()
        if not grid[0][0]:
            dq.append((0,0,1))
            visited.add((0,0))
        while dq:
            r,c,distance=dq.popleft()
            if (r,c)==dest:
                return distance
            for i,j in directions:
                nr=r+i
                nc=c+j
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and grid[nr][nc]==0:
                    dq.append((nr,nc,distance+1))
                    visited.add((nr,nc))
        return -1

