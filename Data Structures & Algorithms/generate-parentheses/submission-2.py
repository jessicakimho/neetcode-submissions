class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(opened, closed):
            # choose, explore, undo
            if opened == closed == n:
                res.append("".join(stack))
                return
            
            if opened < n: # can add "("
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            
            if closed < opened: # can add ")"
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
        