class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        row=len(grid)
        col=len(grid[0])

        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]!=1:
                return 0

            grid[i][j]=0
            area=1
            for x,y in directions:
                area+=dfs(i+x,j+y)
            return area
        
        max_length=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    curr_length=dfs(i,j)
                    max_length=max(curr_length,max_length)
        return max_length