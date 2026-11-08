# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST -> in order traversal -> strictly ascending order
        self.count = 0
        self.answer = None
        def dfs(node):
            if node is None:
                return 
            
            # traverse left subtree
            dfs(node.left)
            if self.answer is not None: # prevents extra work
                return
            
            # process curr node
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return

            # traverse right subtree
            dfs(node.right)
        
        dfs(root)
        return self.answer


