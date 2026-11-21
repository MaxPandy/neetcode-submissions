class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=9,9
        direct=[(0,0),(0,1),(2,0),(1,0),(0,2),(1,1),(1,2),(2,1),(2,2)]
        
        for i in range(row):
            seen=set()
            for j in range(col):
                if board[i][j] in seen:
                    return False
                if board[i][j] != '.':
                    seen.add(board[i][j])

        for j in range(col):
            seen=set()
            for i in range(row):
                if board[i][j] in seen:
                    return False
                if board[i][j] !='.':
                    seen.add(board[i][j])
        
        for i in range(3):
            for j in range(3):
                seen=set()
                for elem in direct:
                    if board[3*i+elem[0]][3*j+elem[1]]!='.' and board[3*i+elem[0]][3*j+elem[1]] in seen:
                        return False
                    if board[3*i+elem[0]][3*j+elem[1]]!='.':
                        seen.add(board[3*i+elem[0]][3*j+elem[1]])

        return True
                    
