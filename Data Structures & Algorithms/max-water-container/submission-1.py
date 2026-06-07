class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights)-1
        while left<right:
            res = max(res, (right-left)*min(heights[left], heights[right]))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return res
        