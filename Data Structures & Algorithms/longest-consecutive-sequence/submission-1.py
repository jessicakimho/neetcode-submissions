class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        numSet = set(nums)

        # num is the start of a sequence if num-1 is not in the set
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest