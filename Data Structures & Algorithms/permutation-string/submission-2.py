class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        refDict = {}
        count={}
        for i, char in enumerate(s1):
            refDict[(ord(char)-ord('a'))] = 1 + refDict.get(ord(char)-ord('a'), 0)
            count[(ord(s2[i])-ord('a'))] = 1 + count.get(ord(s2[i])-ord('a'), 0)
        if count == refDict: return True
        n = len(s1)
        for l in range (1, len(s2)-n+1):
            if count[ord(s2[l-1])-ord('a')] == 1:
                count.pop(ord(s2[l-1])-ord('a'))
            else: count[ord(s2[l-1])-ord('a')] -= 1
            count[ord(s2[l+n-1])-ord('a')] = 1 + count.get(ord(s2[l+n-1])-ord('a'), 0)
            if count == refDict : return True
        return False
        