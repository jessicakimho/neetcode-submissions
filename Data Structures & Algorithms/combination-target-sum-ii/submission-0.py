class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # choose, explore, undo

        candidates.sort()
        res = []
        combo = []

        def backtrack(start, total):
            if total == target:
                res.append(combo.copy())
                return
            if total > target:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: # skip duplicate siblings 
                    continue                                       # allow duplicate descendants i == start
                # choose
                combo.append(candidates[i])   
                # explore
                backtrack(i + 1, total + candidates[i]) # each element can be used once: i + 1, not i
                # undo
                combo.pop()
        
        backtrack(0,0)
        return res