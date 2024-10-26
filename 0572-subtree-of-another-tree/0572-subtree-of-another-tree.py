# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not s: return True
        if not t: return False
        
        if self.sameTree(t,s):
            return True
        
        return (self.isSubtree(t.left,s) or self.isSubtree(t.right,s))
    
    def sameTree(self,p, q):
        if not p and not q:
            return True           
        if  p and q and p.val == q.val:
            return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
        else:
            return False
    
#     class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True
#         if not root:
#             return False

#         if self.isSameTree(root, subRoot):
#             return True
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if p and q and p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         else:
#             return False