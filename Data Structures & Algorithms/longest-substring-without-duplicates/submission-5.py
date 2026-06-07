class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChain={}
        maxFound=0
        begin, end =0,0
        for i in range(len(s)):
            if s[i] not in curChain:
                curChain[s[i]]=i
                end=i
            else:
                maxFound = max(maxFound, len(curChain))
                for char in s[begin:curChain[s[i]]]:
                    curChain.pop(char)
                begin=curChain[s[i]]+1
                end=i
                curChain[s[i]]=i
        return max(maxFound, len(curChain))