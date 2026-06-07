class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range (len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            if sortedStr not in hashMap:
                hashMap[sortedStr] = []
            hashMap[sortedStr].append(strs[i])
        return [x for x in hashMap.values()]


        