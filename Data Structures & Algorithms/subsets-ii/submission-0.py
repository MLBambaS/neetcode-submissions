class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(start, current):
            res.append(current[:])
            for i in range(start, len(nums)):
                # Sauter les doublons au même niveau de récursion
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtracking(i+1, current)
                current.pop()
                prev = nums[i]
        backtracking(0, [])
        return res
        