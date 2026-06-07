class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, freq= {}, defaultdict(list)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key,v in count.items():
            freq[v].append(key)
        res, i = [], len(nums)
        while len(res)<k:
            res.extend(freq[i])
            i-=1
        return res
