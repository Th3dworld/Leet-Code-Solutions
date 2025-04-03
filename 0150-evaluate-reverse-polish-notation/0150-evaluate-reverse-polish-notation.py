class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            match token:
                case "+":
                    second, first= int(stack.pop()), int(stack.pop())
                    stack.append(first + second)
                case "-":
                    second, first= int(stack.pop()), int(stack.pop())
                    stack.append(first - second)
                case "*":
                    second, first= int(stack.pop()), int(stack.pop())
                    stack.append(first * second)
                case "/":
                    second, first= int(stack.pop()), int(stack.pop())
                    stack.append((first / second))
                case _:
                    stack.append(token)
        
        return int(stack[0])