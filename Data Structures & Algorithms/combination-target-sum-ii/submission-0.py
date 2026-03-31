class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combo = []

        def dfs(i, combo, total_so_far):

            if total_so_far == target:
                res.append(combo.copy())
                return 

            if i == len(candidates) or total_so_far > target:
                return

            
            # include duplicate candidates
            combo.append(candidates[i])
            dfs(i+1, combo, total_so_far + candidates[i])

            combo.pop()
            # skip duplicate candidates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i = i + 1
            
            dfs(i+1,combo, total_so_far )
        dfs(0, [], 0)
        return res




