class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # can contain duplicates unlike Subsets I
        nums.sort()
        res = []
        subset = []

        def backtrack(start):
            res.append(subset.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # choose
                subset.append(nums[i])
                # explore
                backtrack(i + 1)
                # undo
                subset.pop()
        
        backtrack(0)
        return res
        
