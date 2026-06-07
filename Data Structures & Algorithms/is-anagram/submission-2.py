class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        if len(s) != len(t):
            return False
        for i in range (len(s)):
            if s[i] in dict1:
                dict1[s[i]] +=1
            else:
                dict1[s[i]] = 1
        for j in range (len(t)):
            if t[j] in dict2:
                dict2[t[j]] +=1
            else:
                dict2[t[j]] = 1
        for x in dict1:
            if x not in dict2:
                return False
            else:
                if dict1[x] != dict2[x]: return False
        return True
        
        