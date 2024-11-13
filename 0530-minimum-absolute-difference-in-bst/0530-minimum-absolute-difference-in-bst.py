# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        order = []
        small = float("inf")
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            order.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        if len(order) == 1:
            return inorder[0]
        
        order.sort()
        l,r = 0,1
        
        while r < len(order):
            small = min(small, abs(order[r] - order[l]))
            l += 1
            r += 1
            
        return small