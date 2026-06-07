class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i], speed[i]) for i in range(len(speed))]
        arr.sort(reverse=True)
        stack = []
        for i in range(len(arr)):
                t = (target-arr[i][0])/arr[i][1]
                if not stack or stack[-1]<t:
                        stack.append(t)
        return len(stack) 
        