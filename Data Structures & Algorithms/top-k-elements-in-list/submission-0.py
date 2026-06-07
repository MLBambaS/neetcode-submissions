class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = 1 + count.get(x, 0)
        res = [0]*k
        for i in range (k):
            curMax, curCount = list(count.items())[0]
            for x,y in count.items():
                if y > curCount:
                    curMax, curCount = x, y
            count.pop(curMax)
            res[i] = curMax
        return res

        