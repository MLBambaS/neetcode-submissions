class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackVal = stack.pop()
                res[stackInd] = i-stackInd
            stack.append([i,t])
        return res
        