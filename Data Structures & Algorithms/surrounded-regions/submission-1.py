class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(row,col):
            safe.add((row,col))
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                r, c = row+dr, col+dc
                if 0<=r<ROWS and 0<=c<COLS and board[r][c]=='O' and (r,c) not in safe:
                    dfs(r,c)
        for col in range(COLS):
            if board[0][col]=='O': dfs(0,col)
            if board[ROWS-1][col]=='O': dfs(ROWS-1,col)
        for row in range(ROWS):
            if board[row][0]=='O': dfs(row,0)
            if board[row][COLS-1]=='O': dfs(row,COLS-1)
        
        for r in range (1, ROWS-1):
            for c in range (1, COLS-1):
                if board[r][c]=='O' and (r,c) not in safe:
                    board[r][c] = 'X'