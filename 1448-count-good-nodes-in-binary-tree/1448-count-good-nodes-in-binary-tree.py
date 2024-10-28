# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        self.count = 0
        
        def dfs(curr, maxVal):
            if not curr:
                return 0
            if curr.val >= maxVal:
                self.count += 1
            maxVal = max(maxVal, curr.val)
            dfs(curr.left, maxVal)
            dfs(curr.right, maxVal)
        dfs(root, root.val)
        return self.count