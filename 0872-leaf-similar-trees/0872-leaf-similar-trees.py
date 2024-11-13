# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        leafs2 = []
        
        def dfs(root, res):
            if not root:
                return 
            
            if not root.left and not root.right:
                res.append(root.val)
            
            dfs(root.left, res)
            dfs(root.right, res)
        
        dfs(root1, leafs1)
        dfs(root2, leafs2)
        
        return leafs1 == leafs2