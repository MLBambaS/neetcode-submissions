class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        leftMax, rightMax = 0, [0]*len(height)
        for i in range(len(height)-2, -1, -1):
                rightMax[i] = max(rightMax[i+1], height[i+1]) 
        water = 0
        for i in range(len(height)):
                if min(leftMax, rightMax[i]) > height[i]:
                        water+=min(leftMax, rightMax[i])-height[i]
                leftMax = max(leftMax, height[i])
        return water