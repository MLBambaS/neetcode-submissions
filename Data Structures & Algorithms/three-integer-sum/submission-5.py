class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        for i,num in enumerate(nums):
                if num in seen:
                        continue
                seen.add(num)
                left, right = i+1, len(nums)-1
                while left<right:
                        s = nums[left]+nums[right]
                        if left<right and s+num < 0:
                                left+=1
                        elif left<right and s+num > 0:
                                right-=1
                        else: 
                                res.append([num, nums[left], nums[right]])
                                while left+1<right and nums[left]==nums[left+1]:
                                        left+=1
                                left+=1
                                while left+1< right and nums[right]==nums[right-1]:
                                        right-=1
                                right-=1
        return res