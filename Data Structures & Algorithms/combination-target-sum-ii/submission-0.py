class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(start, currentList, currentSum):
            if currentSum == target:
                res.append(currentList[:])
                return
            if currentSum > target: return
            prev =-1 # to avoid treating duplicates
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num == prev:
                    continue
                currentSum+=num
                currentList.append(num)

                backtracking(i+1, currentList, currentSum)
                currentSum-=num
                currentList.pop()
                prev = num
        backtracking(0, [], 0)
        return res
        