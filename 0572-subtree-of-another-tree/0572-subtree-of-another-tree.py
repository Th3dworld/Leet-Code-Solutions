# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub:
            return True
        if not root:
            return False
        
        if self.isSameTree(root,sub):
            return True
        
        return self.isSubtree(root.right, sub) or self.isSubtree(root.left, sub) 
    
    def isSameTree(self, root, sub):
        if not root and not sub:
            return True
        elif not root or not sub or sub.val != root.val:
            return False
        else:
            return self.isSameTree(root.right, sub.right) and self.isSameTree(root.left, sub.left)
        