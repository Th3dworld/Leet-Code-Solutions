class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[","}":"{",")":"("}
        stack = []
        
        for c in s:
            if c in closeToOpen:
                if len(stack) > 0 and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
            
        