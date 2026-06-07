class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end
        while start <= end:
            middle = start + (end-start)//2
            numHours = 0
            for p in piles:
                numHours += math.ceil(p/middle)
            if numHours <= h:
                res = middle
                end = middle-1
            else:
                start = middle+1
        return res