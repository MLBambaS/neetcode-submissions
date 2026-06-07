class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n-1):
            val = temperatures[i]
            j = i+1
            if temperatures[j]>val: res[i] = 1
            else:
                while j<n:
                    if temperatures[j]>val: 
                        res[i] = j-i 
                        break
                    else: j=j+1
        return res
        