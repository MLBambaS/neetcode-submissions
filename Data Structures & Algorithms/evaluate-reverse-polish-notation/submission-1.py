class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left+right)
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif token == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left*right)
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append((int)(left/right))
            else:
                stack.append((int) (token))
        return stack.pop()