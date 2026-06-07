class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
                if c =='+':
                        val = stack.pop()+stack.pop()
                        stack.append(val)
                elif c =='*':
                        val = stack.pop()*stack.pop()
                        stack.append(val)
                elif c == '-':
                        r = stack.pop()
                        l = stack.pop()
                        val = l - r
                        stack.append(val)
                elif c == '/':
                        r = stack.pop()
                        l = stack.pop()
                        val = l / r
                        stack.append(int(val))
                else:
                        stack.append(int(c))
        return stack.pop()