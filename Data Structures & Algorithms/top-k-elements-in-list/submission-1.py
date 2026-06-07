class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        invFreq = {i:[] for i in range(1, len(nums)+1)}
        for num, count in freq.items():
            invFreq[count].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for j in invFreq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        