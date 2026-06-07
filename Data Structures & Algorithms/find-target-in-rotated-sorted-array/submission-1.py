class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target: return 0
        if nums[len(nums)-1] == target: return len(nums)-1
        l, r = 0, len(nums)-1
        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target: return m
            if target < nums[m]:
                if target >= nums[l]: r = m-1
                else:
                    if nums[l] <= nums[m]:
                        l=m+1
                    else: r = m-1
            else:
                if target <= nums[r]: l=m+1
                else:
                    if nums[m] >= nums[r]:
                        l = m+1
                    else: r = m-1
        return -1
