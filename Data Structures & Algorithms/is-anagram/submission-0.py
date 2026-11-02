class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency counting
        # if both words have the same character frequency counts, they are anagrams

        s_freq = {}
        t_freq = {}

        for c in s:
            s_freq[c] = s_freq.get(c, 0) + 1
        
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        return s_freq == t_freq