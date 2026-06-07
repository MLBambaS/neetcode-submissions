class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = nums[0]
        zeroCount=0
        for i in range(1, len(nums)):
            if nums[i]!=0:
                prod *= nums[i]
            else: zeroCount += 1
        if zeroCount > 1:
            return [0]*(len(nums))
        elif zeroCount == 1:
            res = [0]*(len(nums))
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
                    return res
        res = []
        for x in nums:
            res.append(int(prod/x))
        return res
            
        