class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisMap = {")":"(", "]":"[", "}":"{"}
        stack = []

        for ch in s:
            if ch in parenthesisMap:
                if stack and parenthesisMap[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if not stack:
            return True
        else:
            return False
                