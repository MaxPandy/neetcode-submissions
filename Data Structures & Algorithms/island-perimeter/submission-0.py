class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack=[]
        neig=[(0,1),(1,0),(-1,0),(0,-1)]
        row=len(grid)
        col=len(grid[0])
        m=[[0]*(col+2) for i in range (row+2)]
        for i in range (row):
            for j in range(col):
                m[i+1][j+1]=grid[i][j]
        total=0

        for i in range (1,row+1):
            for j in range(1,col+1):
                if m[i][j]:
                    total+=4-m[i+1][j]-m[i][j+1]-m[i-1][j]-m[i][j-1]
        return total
                    