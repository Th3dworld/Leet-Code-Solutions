# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inorder = []
        small = float("inf")
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        l,r = 0,1
        
        while r < len(inorder):
            small = min(small, inorder[r] - inorder[l])
            l += 1
            r += 1
        
        return small