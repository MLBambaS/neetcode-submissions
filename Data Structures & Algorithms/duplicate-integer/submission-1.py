class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        asASet = set(nums);
        return len(asASet) != len (nums) 

        