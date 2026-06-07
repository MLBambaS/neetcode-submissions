class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1: return len(s)
        res = 1
        start = 0
        seen = set(s[0])
        for end in range(1, len(s)):
                if s[end] in seen:
                        while s[start] != s[end]:
                                seen.remove(s[start])
                                start+=1
                        start+=1
                else:
                        seen.add(s[end])
                        res = max(len(seen), res)
        return res
        