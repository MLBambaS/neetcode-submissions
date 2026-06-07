class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {(x,y): [] for x,y in points}
        for i in range(len(points)-1):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                d = abs(x1-x2)+abs(y1-y2)
                graph[(x1,y1)].append((d, (x2,y2)))
                graph[(x2,y2)].append((d, (x1,y1)))

        minHeap=[(0, (points[0][0], points[0][1]))] 
        visited = set()
        cost=0
        while len(visited) < len(points):
            (c,(x,y)) = heapq.heappop(minHeap)
            if (x,y) in visited:
                continue
            cost+=c
            visited.add((x,y))
            for (c2, (x2, y2)) in graph[(x,y)]:
                if (x2,y2) not in visited:
                    heapq.heappush(minHeap, (c2, (x2, y2)))
        return cost






        