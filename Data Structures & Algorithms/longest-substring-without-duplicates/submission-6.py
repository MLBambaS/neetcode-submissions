class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChain={}
        maxFound=0
        begin=0
        for i in range(len(s)):
            if s[i] in curChain and begin<=curChain[s[i]]:
                begin=curChain[s[i]]+1
            else:
                maxFound=max(maxFound, i-begin+1)
            curChain[s[i]] = i
        return maxFound