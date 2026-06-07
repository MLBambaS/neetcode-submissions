class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freqDict1, freqDict2 = {}, {}
        for i in range(len(s)):
            freqDict1[s[i]] = 1 + freqDict1.get(s[i], 0)
            freqDict2[t[i]] = 1 + freqDict2.get(t[i], 0)
        return freqDict1 == freqDict2
        