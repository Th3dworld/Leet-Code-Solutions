# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        
        def dfs(root):
            if not root:
                return
            
            if root.val in count:
                count[root.val] += 1
            else:
                count[root.val] = 1
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res = []
        mode = 0
        
        for k,v in count.items():
            mode = max(mode, v)
        
        for k,v in count.items():
            if v == mode:
                res.append(k)
        
        return res