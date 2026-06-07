class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for i in range(len(nums)):
            if nums[i] in dico: return [dico[nums[i]], i]
            dico[target-nums[i]]=i        
        