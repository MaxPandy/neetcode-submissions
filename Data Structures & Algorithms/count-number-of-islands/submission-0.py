class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number=0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    number+=1
                    stack=[(i,j)]
                    grid[i][j]=0
                    while stack:
                        r,c=stack.pop()
                        for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                            if 0<=r+x<len(grid) and 0<=c+y<len(grid[0]) and grid[r+x][c+y]=='1':
                                stack.append((r+x,c+y))
                                grid[r+x][c+y]=0
        return number
