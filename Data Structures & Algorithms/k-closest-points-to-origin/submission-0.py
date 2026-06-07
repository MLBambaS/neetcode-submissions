class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = {}
        for p in points:
            d = math.sqrt(p[0]**2 + p[1]**2)
            if d in hashMap:
                hashMap[d].append(p)
            else:
                hashMap[d] = [p]
        heap = list(hashMap.keys())
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            d = heapq.heappop(heap)
            if len(hashMap[d]) <= k-len(res):
                res.extend(hashMap[d])
            else:
                for i in range(k-len(res)):
                    res.append(hashMap[d][i])
        return res
        