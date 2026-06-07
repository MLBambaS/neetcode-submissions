class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Créer un tas min avec (distance, point)
        min_heap = []
        for point in points:
            # Pas besoin de sqrt pour comparer les distances
            dist = point[0]**2 + point[1]**2
            heapq.heappush(min_heap, (dist, point))
        
        # Extraire les k points les plus proches
        result = []
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result