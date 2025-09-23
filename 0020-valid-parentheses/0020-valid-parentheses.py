class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {"]":"[", "}":"{", ")":"("}
        stack = []

        for p in s:
            if p in closedToOpen:
                if stack and stack[-1] == closedToOpen[p]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(p)

        return not stack