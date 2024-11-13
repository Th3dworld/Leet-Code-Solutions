# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        print
        for i in range(len(inorder)):
            if i == 0:
                root = TreeNode(inorder[i])
                curr = root
            else:
                curr.right = TreeNode(inorder[i]) 
                curr = curr.right
        
        return root
        