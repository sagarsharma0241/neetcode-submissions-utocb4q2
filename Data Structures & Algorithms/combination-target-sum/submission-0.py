class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, total_so_far):

            if total_so_far == target:
                res.append(combo.copy())
                return

            if i >= len(nums) or total_so_far > target:
                return

            combo.append(nums[i])
            dfs(i, combo, total_so_far + nums[i])

            combo.pop()
            dfs(i + 1, combo, total_so_far)

        dfs(0, [], 0)
        return res

        