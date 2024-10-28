# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val >= q.val:
            big = p.val
            small = q.val
        else:
            big = q.val
            small = p.val
        def dfs(curr):
            if curr.val >= small and curr.val <= big:
                return curr
            elif curr.val > big:
                return dfs(curr.left)
            elif curr.val < small:
                return dfs(curr.right)
        return dfs(root)