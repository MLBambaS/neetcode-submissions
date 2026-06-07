class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        head, tail = 0, len(heights)-1
        while(head<tail):
            area = max(area, (min(heights[head], heights[tail])*(tail-head)))
            if heights[head] < heights[tail]:
                head+=1
            else: 
                tail-=1
        return area

        