class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(nums: List[int], target:int, start: int, end: int) -> int:
            if nums[start] > target or nums[end] < target:
                return -1
            middle = start + int((end-start)/2)
            if nums[middle] == target: return middle
            elif nums[middle] < target: return recursive(nums, target, middle+1, end)
            else: return recursive(nums, target, start, middle-1)

        return recursive(nums, target, 0, len(nums)-1)