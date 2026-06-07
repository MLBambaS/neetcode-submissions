class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        refCount = {}
        count={}
        for char in t:
            refCount[ord(char)-ord('A')] = 1 + refCount.get(ord(char)-ord('A'), 0)
        for n in range(len(t), len(s)+1):
            for l in range (len(s)-n+1):
                count = {}
                for i in range (l, l+n):
                    count[ord(s[i])-ord('A')] = 1 + count.get(ord(s[i])-ord('A'), 0)
                if self.dictIncludes(refCount, count):
                    return s[l: l+n]
        return ""
    
    def dictIncludes(self, smaller:dict, larger: dict) -> bool:
        if len(smaller) > len(larger): return False
        for key, val in smaller.items():
            if key not in larger.keys() or larger[key] < val:
                return False
        return True