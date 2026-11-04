# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs, pre-order
        # add node values into a list
        # check if both lists match
        # structure matches if node is None
        
        def sameTree(node1, node2):

            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False
                
            if node1.val != node2.val:
                return False

            left = sameTree(node1.left, node2.left)
            right = sameTree(node1.right, node2.right)

            return (left and right)

        def dfs(node):
            
            if node is None:
                return False

            if sameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        if subRoot is None:
            return True
        
        return dfs(root)

            
        
      
            

            