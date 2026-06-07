class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        maps = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        def backtracking(current):
            if len(current)==len(digits):
                res.append(current)
                return
            i = len(current)
            digit = digits[i]
            for j in maps[digit]:
                current+=j
                backtracking(current)
                current = current[:len(current)-1]
        backtracking("")
        return res


        