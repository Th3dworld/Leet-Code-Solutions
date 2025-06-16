class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            elif stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        
        return not stack