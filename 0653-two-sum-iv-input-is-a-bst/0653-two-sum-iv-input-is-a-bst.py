# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashSet = set()
        def dfs(root):
            if not root:
                return False
            
            if k - root.val in hashSet:
                return True
            
            hashSet.add(root.val)
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)