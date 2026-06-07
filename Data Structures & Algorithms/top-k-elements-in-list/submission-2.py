class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+count.get(num, 0)
        n = len(nums)
        freq = defaultdict(list)
        for x,y in count.items():
            freq[y].append(x)
        res, j = [], n
        while len(res)<k:
            if j in freq:
                res.extend(freq[j])
            j-=1
        return res

        