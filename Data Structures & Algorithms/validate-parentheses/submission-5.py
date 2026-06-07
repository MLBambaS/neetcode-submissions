class Solution:
    def isValid(self, s: str) -> bool:
        dico = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
                if c in dico:
                        if not stack: return False
                        x = stack.pop()
                        if dico[c] != x: return False
                else:
                        stack.append(c)
        return not stack