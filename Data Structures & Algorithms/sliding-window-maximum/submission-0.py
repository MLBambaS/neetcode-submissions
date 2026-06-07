import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []
        for i in range(k):
            heapq.heappush(maxHeap, (-1*nums[i], i))
        res.append(-1*maxHeap[0][0])
        r = k
        while r < len(nums):
            heapq.heappush(maxHeap, (-1*nums[r], r))
            while not r-k <maxHeap[0][1]<= r:
                heapq.heappop(maxHeap)
            res.append(-1*maxHeap[0][0])
            r+=1
        return res
            