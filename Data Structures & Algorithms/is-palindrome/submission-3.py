class Solution:
    def isPalindrome(self, s: str) -> bool:
        # have two pointers, one starting in the beginning, one at the end
        # as we move the pointers towards each other, check if the characters they're pointing to are the same
        # if they aren't its not a palindrome

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
