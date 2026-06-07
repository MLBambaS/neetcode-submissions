class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        start = 0
        res = 0
        for end in range(len(s)):
                freqDict[s[end]] = 1 + freqDict.get(s[end], 0)
                maxFreq = freqDict[s[end]]
                for c in freqDict:
                        if freqDict[c] > maxFreq: 
                                maxFreq = freqDict[c]
                if end-start+1-maxFreq <= k:
                        res = max(res, end-start+1)
                else:
                        freqDict[s[start]] -= 1
                        start +=1
        return res

