class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS,COLS = len(heights), len(heights[0])
        def dfs(r,c,visited):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited:
                return
            visited.add((r,c))
            for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                if 0<=r+dr<ROWS and 0<=c+dc<COLS and heights[r][c] <= heights[r+dr][c+dc]:
                    dfs(r+dr,c+dc,visited)
        for col in range(COLS):
            dfs(0,col,pac)
            dfs(ROWS-1,col,atl)
        for row in range(ROWS):
            dfs(row,0,pac)
            dfs(row,COLS-1,atl)
        return list(pac.intersection(atl))

        