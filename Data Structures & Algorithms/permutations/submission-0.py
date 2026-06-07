class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        already =[False for i in range(len(nums))]
        def backtracking(start, current, already):
            if len(current) == len(nums):
                res.append(current[:])
                return
            for i in range(len(nums)):
                if already[i]:
                    continue
                already[i] = True
                current.append(nums[i])
                backtracking(i+1, current, already)
                current.pop()
                already[i] = False
        backtracking(0, [], already)
        return res            
        