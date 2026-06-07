class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            head, tail = i+1, len(nums)-1
            target=-nums[i]
            while(head<tail):
                sumC = nums[head]+nums[tail]
                if sumC == target:
                        res.append([nums[i], nums[head], nums[tail]])
                        while(head<tail and nums[head]==nums[head+1]):
                            head+=1
                        while(head<tail and nums[tail]==nums[tail-1]):
                            tail-=1
                        head+=1
                        tail-=1
                elif sumC<target:
                    head+=1
                elif sumC>target:
                    tail-=1

        return res
        