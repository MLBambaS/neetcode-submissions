class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNum = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in dictNum: return [dictNum[rest], i]
            else:
                dictNum[num] = i
        