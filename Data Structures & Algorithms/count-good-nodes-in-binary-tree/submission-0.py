# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # path -> dfs
        self.count = 0

        def dfs(node, max_value):
            if node is None:
                return 0
            
            if node.val >= max_value:
                self.count += 1
            
            max_value = max(max_value, node.val)

            dfs(node.left, max_value)
            dfs(node.right, max_value)
        
        dfs(root, root.val)
        return self.count
            
