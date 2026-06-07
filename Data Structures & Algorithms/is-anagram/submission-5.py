class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        dicT, dicS = {}, {}
        for i in range(len(s)):
            dicT[t[i]] = 1+dicT.get(t[i], 0)
            dicS[s[i]] = 1+dicS.get(s[i], 0)
        for k in dicS.keys():
            if k not in dicT or dicS[k] != dicT[k]:
                return False
        return True