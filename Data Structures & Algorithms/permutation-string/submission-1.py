class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        refDict = {}
        for char in s1:
            refDict[(ord(char)-ord('a'))] = 1 + refDict.get(ord(char)-ord('a'), 0)
        n = len(s1)
        for l in range (len(s2)-n+1):
            count={}
            for i in range(l, l+n):
                count[ord(s2[i])-ord('a')] = 1 + count.get(ord(s2[i])-ord('a'), 0)
            if count == refDict : return True
        return False
        