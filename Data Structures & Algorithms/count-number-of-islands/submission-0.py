class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, visited):
            if r<0 or c<0 or r==len(grid) or c==len(grid[0]) or (r,c) in visited or grid[r][c]=="0":
                return
            visited.add((r,c))
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c-1,visited)
            dfs(r,c+1,visited)
        count = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1' and (row, col) not in visited:
                    count+=1
                    dfs(row, col, visited)
        return count
         