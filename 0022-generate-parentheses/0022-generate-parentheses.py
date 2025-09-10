class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def makeParen(opening, closing, stack):
            if opening == closing == n:
                res.append("".join(stack))
            if opening < n:
                stack.append("(")
                makeParen(opening + 1, closing, stack)
                stack.pop()
            if closing < opening:
                stack.append(")")
                makeParen(opening, closing + 1, stack)
                stack.pop()

        makeParen(0, 0, [])
        return res