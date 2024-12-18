# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        total = 0
        
        while q:
            node = q.popleft()
            total += 1
            
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        
        return total