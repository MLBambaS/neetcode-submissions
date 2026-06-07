class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValid(k) -> bool:
            val = 0
            for x in piles:
                val += math.ceil(x/k)
            return val <= h 

        l, r = 1, max(piles)
        while l<r:
            m = (l+r)//2
            if isValid(m):
                r = m
            else:
                l = m+1
        return l
            