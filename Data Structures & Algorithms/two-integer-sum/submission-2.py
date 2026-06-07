class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCopy = [(nums[i], i) for i in range(len(nums))]
        numsCopy.sort()
        left, right = 0, len(nums)-1
        while left < right:
            val = numsCopy[left][0]+numsCopy[right][0]
            if val == target: 
                return[min(numsCopy[left][1], numsCopy[right][1]), max(numsCopy[left][1], numsCopy[right][1])]
            elif val < target: left+=1
            else : right-=1
        