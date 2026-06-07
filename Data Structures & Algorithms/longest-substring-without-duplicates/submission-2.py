class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChain=""
        maxFound=0
        for char in s:
            pos=curChain.find(char)
            if pos==-1:
                curChain+=char
            else:
                maxFound = max(maxFound, len(curChain))
                if pos == len(curChain)-1: 
                    curChain=curChain[pos]
                else: curChain = curChain[pos+1:]+char
        maxFound = max(maxFound, len(curChain))
        return maxFound