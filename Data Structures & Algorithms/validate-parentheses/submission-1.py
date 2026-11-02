class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {"(":")", "[":"]", "{":"}"}
        stack = []

        for c in s:
            if c in bracket_map:
                stack.append(c)
            elif stack and c == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False

        return not stack