# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr: return [True, 0]
            
            right = dfs(curr.right)
            left = dfs(curr.left)
            balanced = right[0] and left[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, 1 + max(left[1],right[1])]
        return dfs(root)[0]