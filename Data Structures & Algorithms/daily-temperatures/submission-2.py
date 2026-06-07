class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
                while stack and stack[-1][1] < temperatures[i]:
                        ind, val = stack.pop()
                        res[ind] = i - ind
                stack.append((i, temperatures[i]))
        return res 