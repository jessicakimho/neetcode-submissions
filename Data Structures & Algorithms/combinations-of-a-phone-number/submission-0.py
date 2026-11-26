class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        path = []

        if digits == "":
            return res

        def backtrack(start):
            if start == len(digits):
                res.append("".join(path))
                return
            # choices: first letter, then second letter, etc
            # for every digit, explore each possible value, undo
            num = digits[start]
            for value in hashmap.get(num):
                path.append(value)
                backtrack(start + 1)
                path.pop()
        
        backtrack(0)
        return res
