class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(r, c, visited, index):
            if r<0 or c<0 or r==len(board) or c==len(board[0]) or (r,c) in visited or board[r][c] != word[index]:
                return False
            if index == len(word)-1:
                return True
            index+=1
            visited.add((r,c))
            if backtracking(r+1,c,visited, index) or backtracking(r,c+1,visited, index) or backtracking(r-1, c, visited, index) or backtracking(r,c-1,visited, index):
                return True
            visited.remove((r,c))
            index-=1
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtracking(r,c,set(), 0): return True
        return False
        
        