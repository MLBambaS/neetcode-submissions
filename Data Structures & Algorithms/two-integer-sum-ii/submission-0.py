class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        for i in range (size):
            diff = target - numbers[i]
            head, tail = i+1, size-1
            if(numbers[tail]< diff or numbers[head]>diff):
                continue
            while(head<tail):
                if numbers[head] == diff: return [i+1, head+1]
                if numbers[tail] == diff: return [i+1, tail+1]
                midd = (head+tail)//2
                if numbers[midd] == diff: return [i+1, midd+1]
                if numbers[midd] > diff:
                    tail = midd-1
                if numbers[midd] < diff:
                    head = midd+1
            if numbers[head] == diff: return [i+1, head+1]


            

        