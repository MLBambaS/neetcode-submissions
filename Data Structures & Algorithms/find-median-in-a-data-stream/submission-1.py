class MedianFinder:

    def __init__(self):
        self.arr = []
        self.leftheap, self.rightheap = [], [] #left étant un maxHeap et right un minHeap
        self.n1, self.n2 = 0,0
        

    def addNum(self, num: int) -> None:
        if self.n1 == self.n2: 
            if self.n1 == 0: #first add
                heapq.heappush(self.leftheap, -1*num)
                self.n1=1
            else:
                if num >= -1*self.leftheap[0]:
                    heapq.heappush(self.rightheap, num)
                    self.n2+=1
                else: 
                    heapq.heappush(self.leftheap, -1*num)
                    self.n1+=1
        elif self.n1 > self.n2:
            if num >= -1*self.leftheap[0]:
                heapq.heappush(self.rightheap, num)
                self.n2+=1
            else:
                val = -1*heapq.heappop(self.leftheap)
                heapq.heappush(self.rightheap, val)
                self.n2+=1
                heapq.heappush(self.leftheap, -1*num)
        else:
            if num <= self.rightheap[0]:
                heapq.heappush(self.leftheap, -1*num)
                self.n1+=1
            else:
                val = -1*heapq.heappop(self.rightheap)
                heapq.heappush(self.leftheap, val)
                self.n1+=1
                heapq.heappush(self.rightheap, num)
        

    def findMedian(self) -> float:
        if self.n1 == self.n2:
            m = -1*self.leftheap[0] + self.rightheap[0]
            return m/2
        else:
            if self.n1 > self.n2: return -self.leftheap[0]
            return self.rightheap[0]
        
        