class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
            
    def add(self, val: int) -> int:
        # Ajouter la valeur au tas
        heapq.heappush(self.min_heap, val)
        
        # Si le tas dépasse k éléments, retirer le plus petit
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # Le plus petit élément du tas est le k-ième plus grand
        return self.min_heap[0]