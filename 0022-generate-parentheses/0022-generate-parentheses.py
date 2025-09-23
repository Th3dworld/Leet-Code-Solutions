class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def genParenth(Open, Closed, stack):
            if Open == Closed == n:
                res.append("".join(stack))
            if Open < n:
                stack.append("(")
                genParenth(Open + 1, Closed, stack)
                stack.pop()
            if Closed < Open:
                stack.append(")")
                genParenth(Open, Closed + 1, stack)
                stack.pop()

        genParenth(0,0,[])
        return res