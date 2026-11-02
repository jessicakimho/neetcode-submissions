# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs, bottom up
        # path length at a node is left subtree height + right subtree height

        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            path_length = left_height + right_height

            self.diameter = max(path_length, self.diameter)

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter