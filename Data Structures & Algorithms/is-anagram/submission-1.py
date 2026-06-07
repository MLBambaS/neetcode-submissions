class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = list(s)
        l1.sort()
        l2 = list(t)
        l2.sort()
        for i in range (len(s)):
            if l1[i] != l2[i]:
                return False
        return True  
        