class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord('a')] += 1
            keyDict = tuple(count)
            if keyDict not in hashMap:
                hashMap[keyDict] = []
            hashMap[keyDict].append(s)
        return list(hashMap.values())


        