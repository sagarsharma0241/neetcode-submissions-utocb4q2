# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            res_left = dfs(root.left)
            res_right = dfs(root.right)

            balanced = (abs(res_left[1] - res_right[1]) <= 1) and res_left[0] and res_right[0]
            return [balanced, 1+ max(res_left[1], res_right[1])]
        return dfs(root)[0]        