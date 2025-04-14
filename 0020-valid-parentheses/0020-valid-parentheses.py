class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"]":"[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c in hashMap:
                if stack and hashMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        
        return not stack