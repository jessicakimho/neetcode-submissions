class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # choose, explore, undo

        res = []
        combo = []

        def backtrack(start, total):
            if total == target:
                res.append(combo.copy())
                return 
            
            if total > target:
                return
            for i in range(start, len(nums)):
                # choose
                combo.append(nums[i])
                # explore
                backtrack(i, total + nums[i])
                # undo
                combo.pop()
        
        backtrack(0,0)
        return res