class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dico:
                return [dico[diff],i]
            dico[num] = i