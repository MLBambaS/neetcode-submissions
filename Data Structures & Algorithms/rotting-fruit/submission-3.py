from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        distance = 0
        freshCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshCount+=1
        if freshCount == 0: return 0
        while queue and freshCount > 0:
            l = len(queue)
            distance+=1
            for i in range(l):
                (row,col) = queue.popleft()
                for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    r,c =row+dr,col+dc
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        queue.append((r,c))
                        grid[r][c] = 2
                        freshCount-=1
        return distance if freshCount == 0 else -1
        