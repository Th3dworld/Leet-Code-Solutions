# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_target):
            if not node:
                return False
            
            if not node.right and not node.left:
                return node.val == current_target
            
            return dfs(node.left, current_target - node.val) or dfs(node.right, current_target- node.val)
        
        return dfs(root, targetSum)