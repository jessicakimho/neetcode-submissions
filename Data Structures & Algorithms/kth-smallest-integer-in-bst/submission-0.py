# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST -> in order traversal -> strictly ascending order
        res = []
        def dfs(node):
            if node is None:
                return 
            
            # traverse left subtree
            dfs(node.left)

            # process curr node
            res.append(node.val)

            # traverse right subtree
            dfs(node.right)
        
        dfs(root)
        return res[k-1]


