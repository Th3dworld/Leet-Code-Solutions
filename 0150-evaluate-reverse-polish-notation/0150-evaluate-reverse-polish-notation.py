class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case '+':
                    second,first = stack.pop(),stack.pop()
                    stack.append(first + second)
                case '*':
                    second,first = stack.pop(),stack.pop()
                    stack.append(first * second)
                case '-':
                    second,first = stack.pop(),stack.pop()
                    stack.append(first - second)
                case '/':
                    second,first = stack.pop(),stack.pop()
                    stack.append(int(first/second))
                case _:
                    stack.append(int(t))
        
        return stack[-1]