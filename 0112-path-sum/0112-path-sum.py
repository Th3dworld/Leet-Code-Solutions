# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val
            
            if current_sum == targetSum and not node.left and not node.right:
                return True
            
            left = dfs(node.right, current_sum)
            right = dfs(node.left, current_sum)
            
            return left or right
        
        return dfs(root, 0)