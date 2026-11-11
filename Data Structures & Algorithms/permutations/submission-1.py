class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # choose, explore, undo
        res = []
        permutation = []
        used = set() # keep track of what you've used

        def backtrack():
            if len(nums) == len(permutation):
                res.append(permutation.copy())
                return

            for num in nums:
                if num in used:
                    continue
                # choose
                permutation.append(num)
                used.add(num)
                # explore
                backtrack()
                # undo
                permutation.pop()
                used.remove(num) # those choices need to be available when you backtrack for a different branch

        backtrack()
        return res

        # time: O(n * n!)
        # space: O(n)