class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        def backtracking(row, current):
            if row == n:
                board = []
                for i in range(n):
                    row_str = '.' * n
                    for r, c in current:
                        if r == i:
                            row_str = row_str[:c] + 'Q' + row_str[c+1:]
                    board.append(row_str)                
                res.append(board)
                return
            for col in range(n):
                if self.isSafe(row, col, current):
                    current.append((row, col))
                    backtracking(row+1, current)
                    current.pop()
        backtracking(0, [])
        return res

    def isSafe(self, row, col, current):
        if not current: return True
        for (r,c) in current:
            if r==row or c==col or abs(row-r)==abs(col-c):
                return False
        return True



        