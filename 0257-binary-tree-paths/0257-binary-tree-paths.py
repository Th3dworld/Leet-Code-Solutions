# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, route):
            if not root:
                return
            
            if not root.right and not root.left:
                route += str(root.val)
                res.append(route)
                return
            
            route += (str(root.val) + "->" )
            
            dfs(root.left, route)
            dfs(root.right, route) 
        
        dfs(root, "")
        return res