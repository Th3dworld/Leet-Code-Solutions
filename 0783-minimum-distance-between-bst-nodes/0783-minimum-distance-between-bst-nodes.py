# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')
        
        # In-order traversal helper function
        def in_order(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order(node.left)
            
            # Update the minimum difference
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            # Traverse the right subtree
            in_order(node.right)
        
        # Start in-order traversal from root
        in_order(root)
        
        return self.min_diff