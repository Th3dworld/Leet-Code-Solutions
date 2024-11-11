# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if (not p or not q) or (p.val != q.val):
#             return False
#         return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
        def dfs(root, arr):
            stack = [root]
            
            while stack:
                node = stack.pop()
                if node:
                    arr.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    arr.append(node)
            
                
        
        pArray, qArray = [], []
        dfs(p, pArray)
        dfs(q, qArray)
        
        print(pArray, qArray)
        return pArray == qArray
        
            