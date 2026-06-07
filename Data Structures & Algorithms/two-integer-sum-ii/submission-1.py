class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail = 0, len(numbers)-1
        while(head < tail):
            sumRes = numbers[head]+numbers[tail]
            if sumRes == target: 
                return [head+1, tail+1]
            if sumRes < target:
                head += 1
            else: 
                tail-=1
            