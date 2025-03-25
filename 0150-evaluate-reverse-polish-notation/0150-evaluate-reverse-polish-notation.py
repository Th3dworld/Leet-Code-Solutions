
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+","-","*","/"])
        stack = []
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                secondVal, firstVal = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(secondVal + firstVal)
                elif t == "-":
                    stack.append(firstVal - secondVal)
                elif t == "*":
                    stack.append(secondVal * firstVal)
                else:
                    if secondVal != 0:
                        stack.append(int(firstVal/secondVal))
                    else:
                        stack.append(firstVal)

        print(stack)
        return stack[-1]