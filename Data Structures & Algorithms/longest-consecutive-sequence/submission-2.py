class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        curMax = 0
        for num in nums:
            if num-1 not in s:
                cur = 1
                x=num
                while x+1 in s:
                    cur+=1
                    x=x+1
                curMax=max(curMax,cur)
        return curMax

        