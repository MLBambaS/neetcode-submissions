class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(start, currentList, currentSum):
            if currentSum == target:
                res.append(currentList[:])
                return
            if currentSum > target: return
            else:
                for i in range(start, len(nums)):
                    currentSum += nums[i]
                    currentList.append(nums[i])
                    backtracking(i, currentList, currentSum)
                    currentSum -= nums[i]
                    currentList.pop()
        backtracking(0, [], 0)
        return res 