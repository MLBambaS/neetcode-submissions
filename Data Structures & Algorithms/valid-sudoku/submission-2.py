class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in seen: return False
                    seen.add(board[r][c])
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] in seen: return False
                    seen.add(board[r][c])
        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range (3*i, 3*(i+1)):
                    for l in range(3*j, 3*(j+1)):
                        if board[k][l] !='.':
                            if board[k][l] in seen: return False
                            seen.add(board[k][l])
        return True
        