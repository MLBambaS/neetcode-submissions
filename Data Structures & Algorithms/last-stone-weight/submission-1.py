class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =[]
        for i in range(len(stones)):
            heap.append(stones[i]*-1)
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x == y: continue
            if x > y: heapq.heappush(heap, y-x)
            else : heapq.heappush(heap, x-y)
        if not heap: return 0
        return heapq.heappop(heap)*-1
        