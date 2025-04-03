class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {"]":"[", "}":"{", ")":"("}
        stack = []

        for ch in s:
            if ch in closedToOpen and len(stack) > 0:
                if closedToOpen[ch] == stack[-1]:
                    stack.pop()
            else:
                stack.append(ch)
        
        return not stack

