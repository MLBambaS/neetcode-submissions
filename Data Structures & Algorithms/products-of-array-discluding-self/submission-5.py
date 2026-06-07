class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftProd, rightProd = [1]*n, [1]*n
        zeroCount = 0
        for i in range(n-1):
            if nums[i]==0:
                if zeroCount == 1: return [0]*n
                zeroCount = 1
            leftProd[i+1] = leftProd[i]*nums[i]
        for j in range(n-1, 0, -1):
            rightProd[j-1] = rightProd[j]*nums[j]
        
        return [leftProd[i]*rightProd[i] for i in range(n)]
