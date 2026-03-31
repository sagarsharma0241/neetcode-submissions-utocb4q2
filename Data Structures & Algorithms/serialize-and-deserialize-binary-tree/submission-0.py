# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return 

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(res)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        print(data)
        input_data = data.split(',')
        print(input_data)

        def dfs():
            if input_data[self.i] == "N":
                self.i = self.i + 1
                return None
            node = TreeNode(int(input_data[self.i]))
            self.i = self.i + 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

       



