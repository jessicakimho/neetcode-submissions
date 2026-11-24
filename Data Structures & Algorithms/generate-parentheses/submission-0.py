class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, opened, closed):
            # choose
            if opened == closed == n:
                res.append(curr)
                return

            # explore
            if opened < n: # can add (
                backtrack(curr + "(", opened + 1, closed)

            if closed < opened: # can add )
                backtrack(curr + ")", opened, closed + 1)
            
        backtrack("", 0, 0)
        return res