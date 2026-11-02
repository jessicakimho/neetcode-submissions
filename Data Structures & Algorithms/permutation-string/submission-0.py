class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) == 0 or len(s1) > len(s2):
            return False
        
        # sliding window + hashtable
        # hashtable for frequency counting
        # slide window until you find a valid permutation -> fixed to size s1

        # get freq map of s1
        freq = {}

        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        window = {}

        # freq map of the first window
        for i in range(len(s1)):
            c = s2[i]
            window[c] = window.get(c, 0) + 1
        
        if window == freq:
            return True

        # initialize pointers
        left = 0
        right = len(s1) - 1

        while right < len(s2) - 1:
            # remove character leaving window
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            
            right += 1
            left += 1

            # add char entering window
            window[s2[right]] = window.get(s2[right], 0) + 1

            if window == freq:
                return True
        
        return False
