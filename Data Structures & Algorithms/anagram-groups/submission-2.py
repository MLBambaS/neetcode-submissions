from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for word in strs:
            charCount = [0]*26
            for c in word:
                i = ord(c)-ord('a')
                charCount[i] += 1
            t = tuple(charCount)
            freq[t].append(word)
        return list(freq.values())
