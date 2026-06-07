class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for u,v,t in times:
            graph[u].append((v,t))
        timesFromK = [float('inf')]*n
        timesFromK[k-1] = 0
        minHeap = [(0,k)]
        while minHeap:
            c, n = heapq.heappop(minHeap)
            if c > timesFromK[n-1]:
                continue
            timesFromK[n-1] = c
            for v,t in graph[n]:
                heapq.heappush(minHeap,(c+t,v))
        maxFound = max(timesFromK)
        if maxFound == float('inf'): return -1
        else: return maxFound
            
        