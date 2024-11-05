# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        leaf1 = []
        stack = [root1]
        
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaf1.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        leaf2 = []
        stack = [root2]
        
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaf2.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return leaf1 == leaf2