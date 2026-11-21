from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid)==len(grid[0])==1 and not grid[0][0]:
            return 1
        directions = [(di, dj) for di, dj in product((-1, 0, 1), repeat=2) if (di, dj) != (0, 0)]
        row=len(grid)
        col=len(grid[0])
        dest=(row-1,col-1)

        visited=set()
        dq=deque()
        if not grid[0][0]:
            dq.append((0,0,1))
            visited.add((0,0))
        while dq:
            r,c,distance=dq.popleft()
            for i,j in directions:
                nr=r+i
                nc=c+j
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and grid[nr][nc]==0:
                    if (nr,nc)==dest:
                        return distance+1
                    dq.append((nr,nc,distance+1))
                    visited.add((nr,nc))
        return -1

