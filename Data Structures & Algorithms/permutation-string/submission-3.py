class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        freq1, freq2 = {}, {}
        for i in range(len(s1)):
                freq1[s1[i]] = 1 + freq1.get(s1[i], 0)
                freq2[s2[i]] = 1 + freq2.get(s2[i], 0)
        if freq1 == freq2: return True
        start, end = 0, len(s1)-1
        while end < len(s2):
                end+=1
                while end < len(s2) and s2[end] not in freq1:
                        end+=1
                        if s2[start] in freq2 and freq2[s2[start]] == 1: freq2.pop(s2[start])
                        elif s2[start] in freq2:
                                freq2[s2[start]] -= 1
                        start+=1
                if end == len(s2): break
                freq2[s2[end]] = 1 + freq2.get(s2[end], 0)
                if s2[start] in freq2 and freq2[s2[start]] == 1 :
                        freq2.pop(s2[start])
                elif s2[start] in freq2:
                        freq2[s2[start]] -= 1
                start+=1
                if freq1 == freq2: return True
        return False