class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <=1 :
            return len(nums)
        values = set(nums)
        curCount, maxCount = 0, 0 
        for x in values:
            if x-1 not in values:
                curCount = 1
                elt=x
                while elt+1 in values:
                    curCount+=1
                    elt+=1
                if curCount>maxCount: maxCount=curCount
        return maxCount
        
        