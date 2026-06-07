class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort(reverse=True)
        stack = []
        for pos, v in pairs:
            if not stack:
                stack.append((pos, v))
            else:
                arrTime = (target - pos) / v
                refTime = (target - stack[-1][0]) / (stack[-1][1])
                if arrTime > refTime:
                    stack.append((pos, v))
                else:
                    continue
        return len(stack)
        