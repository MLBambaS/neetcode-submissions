class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if pairs[opening] != char: return False
        return stack == []

        