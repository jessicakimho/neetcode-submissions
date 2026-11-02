class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers 
        left = 0
        seen = set()

        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            currLength = right - left + 1
            longest = max(currLength, longest)

        return longest