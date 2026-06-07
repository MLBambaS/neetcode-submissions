class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        if start == end: return nums[start]
        if nums[start] < nums[end]: return nums[start]
        if nums[end] < nums[end-1]: return nums[end]
        while start <= end:
            middle = start + (end-start)//2
            if nums[middle-1] > nums[middle] and nums[middle+1] > nums[middle]:
                return nums[middle]
            if nums[middle+1] < nums[middle]:
                return nums[middle+1]
            if nums[start] < nums[middle]:
                start = middle+1
            else: 
                end = middle-1