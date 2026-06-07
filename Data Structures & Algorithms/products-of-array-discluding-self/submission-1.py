class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        leftProduct, rightProduct = [0] * size, [0] * size
        x = 1
        for i in range (size):
            leftProduct[i] = x
            x *= nums[i]
        x = 1
        for j in range(size-1, -1, -1):
            rightProduct[j] = x
            x *= nums[j]
        res = [0] * size
        for i in range(size):
            res[i] = leftProduct[i] * rightProduct[i]
        return res
            