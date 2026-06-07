class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        visited = set()
        def dfs(r,c,visited):
            if r<0 or c<0 or r==len(grid) or c==len(grid[0]) or (r,c) in visited or grid[r][c]==0:
                return 0
            count = 1
            visited.add((r,c))
            count+=dfs(r+1,c,visited)
            count+=dfs(r,c+1,visited)
            count+=dfs(r-1,c,visited)
            count+=dfs(r,c-1,visited)
            return count
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1 and (row,col) not in visited:
                    maxArea=max(maxArea, dfs(row,col,visited))
        return maxArea

        