class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # choose -> explore -> undo
        # decision tree

        res = []
        subset = []

        def backtrack(start):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                # choose
                subset.append(nums[i])
                # explore
                backtrack(i + 1)
                # undo
                subset.pop()
            
        backtrack(0)
        return res