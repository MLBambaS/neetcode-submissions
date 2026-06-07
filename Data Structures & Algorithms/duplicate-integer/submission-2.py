class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqDict = {}
        for num in nums:
            if num in freqDict: return True
            freqDict[num] = 1
        return False
        