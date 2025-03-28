# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not s:
            return True
        
        if not r:
            return False

        if self.isSameTree(r,s):
            return True

        return self.isSubtree(r.right,s) or self.isSubtree(r.left,s)

    def isSameTree(self, r, s) -> bool:
        if not r and not s:
            return True
        
        if not r or not s or r.val != s.val:
            return False
        
        return self.isSameTree(r.right, s.right) and self.isSameTree(s.left, r.left)

