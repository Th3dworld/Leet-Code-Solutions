class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def genCombs(Open,Closed):
            if Open == Closed == n:
                res.append("".join(stack))
                return
            
            if Open < n:
                stack.append("(")
                genCombs(Open+1, Closed)
                stack.pop()
            
            if Closed < Open:
                stack.append(")")
                genCombs(Open, Closed + 1)
                stack.pop()
    
        
        genCombs(0,0)
        return res