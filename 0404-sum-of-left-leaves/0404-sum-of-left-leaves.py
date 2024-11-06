# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if (not root.left and not root.right) or not root:
            return 0
        
        total = 0
        
        q = deque([(root, True)])
        
        while q:
            for i in range(len(q)):
                node, is_leftMost = q.popleft()
                if is_leftMost and not node.left and not node.right:
                    total += node.val
                if node.left:
                    q.append((node.left, True))
                if node.right:
                    q.append((node.right, False))
                    
        return total
                    