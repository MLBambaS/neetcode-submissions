class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0
        left, right = 0, len(heights)-1
        while left<right:
                if heights[left] < heights[right]:
                        curArea = (right-left)*heights[left]
                        curMax = max(curMax, curArea)
                        left+=1
                else:
                        curArea = (right-left)*heights[right]
                        curMax = max(curMax, curArea)
                        right-=1
        return curMax