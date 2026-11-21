class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[rows-1][cols-1]:
            return 0

        memo=[[-1]*cols for _ in range(rows)]

        def dfs(i,j):
            if i==rows-1 and j==cols-1:
                return 1
            if i>=rows or j>=cols or obstacleGrid[i][j]==1:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            memo[i][j]=dfs(i+1,j)+dfs(i,j+1)
            return memo[i][j]
        return dfs(0,0)