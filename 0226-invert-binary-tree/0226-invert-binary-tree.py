# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return node
        
        tmp = node.right
        node.right = node.left
        node.left =tmp
        
        self.invertTree(node.right)
        self.invertTree(node.left)
        
        return node