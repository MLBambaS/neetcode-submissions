class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
                start = i
                while stack and stack[-1][1] > heights[i]:
                        start, val = stack.pop()
                        maxArea = max(maxArea, (i-start)*val)
                stack.append((start, heights[i]))
        while stack:
                start, val = stack.pop()
                maxArea = max(maxArea, (len(heights)-start)*val)
        return maxArea
                
        