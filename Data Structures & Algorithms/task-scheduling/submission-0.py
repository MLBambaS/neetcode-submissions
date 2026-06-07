class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        for x in tasks:
            if x in hashMap: hashMap[x]+=1
            else:
                hashMap[x] = 1
        heap=[]
        for x,y in hashMap.items():
            heapq.heappush(heap, (-1*y,x))
        queue = deque()
        c = 0
        while heap or queue:
            c+=1
            if heap:
                (y,x) = heapq.heappop(heap)
                if y < -1 :
                    hashMap[x] -= 1
                    queue.append((x, c))
                else:
                    hashMap.pop(x)
            if queue:
                (x, count) = queue.popleft()
                if c == count+n:
                    heapq.heappush(heap, (-1*hashMap[x], x))
                else:
                    queue.appendleft((x, count))
        return c


        