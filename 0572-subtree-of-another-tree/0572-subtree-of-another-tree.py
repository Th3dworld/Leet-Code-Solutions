# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not s: return True
        if not r: return False
        
        if self.sameTree(s,r):
            return True
        
        return self.isSubtree(r.right,s) or self.isSubtree(r.left,s)
    
    def sameTree(self,r,s):
        if not r and not s:
            return True
        if not r or not s or s.val != r.val:
            return False
        else:
            return self.sameTree(s.right,r.right) and self.sameTree(s.left,r.left)