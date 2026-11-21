class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows=len(text1)
        cols=len(text2)
        grid=[[0]*(cols) for _ in range(rows)]
        for i in range(rows):
            if text2[0] in text1[:i+1]:
                grid[i][0]=1
        for j in range(cols):
            if text1[0] in text2[:j+1]:
                grid[0][j]=1
        for i in range(1,rows):
            for j in range(1,cols):
                if text1[i]==text2[j]:
                    grid[i][j]=grid[i-1][j-1]+1
                else:
                    grid[i][j]=max(grid[i-1][j],grid[i][j-1])
        return grid[rows-1][cols-1]
