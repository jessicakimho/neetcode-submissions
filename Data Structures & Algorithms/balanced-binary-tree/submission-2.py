# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs, bottom up approach?
        # post-order
        # get left and right subtree height
        # check if difference is > 1 -> false
        # return height of node

        def dfs(node):
            # leaf node has height = 0
            if node is None:
                return 0
            
            left_height = dfs(node.left) # get left subtree height
            right_height = dfs(node.right) # get right subtree height

            # if either subtree is unbalanced, the tree is unbalanced
            if left_height == -1 or right_height == -1:
                return -1

            # is this node unbalanced?
            if abs(left_height - right_height) > 1:
                return -1
            
            # return this node's height
            return 1 + max(left_height, right_height)

        return dfs(root) != -1
        

            