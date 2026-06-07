class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        l,r = 0, n-1
        while l<=r:
            m = (l+r)//2
            if nums[m-1] > nums[m] and nums[(m+1)%n] > nums[m]:
                return nums[m]
            elif nums[r] > nums[m]:
                r = m-1
            else:
                l = m+1
        