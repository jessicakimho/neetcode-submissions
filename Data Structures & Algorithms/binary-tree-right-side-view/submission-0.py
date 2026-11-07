# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs, find right-most node at each level
        res = []

        if root is None:
            return res
        
        queue = deque([root])

        while queue:
            queue_len = len(queue)
            right_most = None
            for i in range(queue_len):
                node = queue.popleft()
                right_most = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(right_most)
        
        return res