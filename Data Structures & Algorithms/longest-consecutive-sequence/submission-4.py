class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        curMax = 0
        for num in s:
                if num-1 in s: continue
                curCount = 1
                cur = num
                while cur+1 in s:
                        curCount += 1
                        cur = cur + 1
                curMax = max(curMax, curCount)
        return curMax
        
            
        