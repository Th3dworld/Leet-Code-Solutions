class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(opened,closed, stack):
            if opened == closed == n:
                res.append("".join(stack))
            if opened < n:
                stack.append("(")
                generate(opened + 1,closed, stack)
                stack.pop()
            if closed < opened:
                stack.append(")")
                generate(opened,closed  + 1, stack)
                stack.pop()
        
        generate(0,0,[])
        return res