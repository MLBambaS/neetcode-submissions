class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd, rightProd = [1]*n, [1]*n
        zeroCount = 0
        for i in range(1, n):
            leftProd[i] = leftProd[i-1]*nums[i-1]
            rightProd[n-1-i] = rightProd[n-i]*nums[n-i]
        res = [0]*n
        for i in range(n):
            res[i] = leftProd[i]*rightProd[i]
        return res
            
        