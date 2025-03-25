class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(OpenN, closedN):
            if OpenN == closedN == n:
                res.append("".join(stack))
                return
            
            if OpenN < n:
                stack.append("(")
                back(OpenN + 1, closedN)
                stack.pop()
            
            if closedN < OpenN:
                stack.append(")")
                back(OpenN, closedN + 1)
                stack.pop()
        
        back(0,0)
        return res