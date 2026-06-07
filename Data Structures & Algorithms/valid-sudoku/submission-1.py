class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            check = [0]*9
            for i in range(9):
                if row[i]!='.':
                    num = int(row[i])
                    if check[num-1]==1: return False
                    check[num-1]=1
        for col in range(9):
            check = [0]*9
            for r in range(9):
                if board[r][col]!='.':
                    num = int(board[r][col])
                    if check[num-1]==1: return False
                    check[num-1]=1
        for i in range(3):
            for j in range(3):
                check = [0]*9
                for r in range(3*i, 3*(i+1)):
                    for c in range(3*j, 3*(j+1)):
                        if board[r][c]!='.':
                            num = int(board[r][c])
                            if check[num-1]==1: return False
                            check[num-1]=1
        return True




        