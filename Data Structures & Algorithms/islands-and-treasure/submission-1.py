class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        distance = 0
        while queue:
            l = len(queue)
            for i in range(l):
                r, c = queue.popleft()
                if grid[r][c] == 2147483647: 
                    grid[r][c] = distance
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == 2147483647:
                        queue.append((r+dr,c+dc))
            distance+=1
        