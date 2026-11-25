class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s): # base case, reached end of the string
                res.append(path.copy())
                return
            
            # choices: partition or skip
            # if curr substring is a palindrome, choose and explore -> else, skip

            for end in range(start, len(s)): # explore every substring
                substring = s[start:end+1]

                if substring == substring[::-1]: # curr substring is a palindrome
                    path.append(substring) # choose
                    backtrack(end + 1) # explore
                    path.pop() # undo

        backtrack(0)
        return res

           