# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            maximum = float("-inf")
            
            for i in range(len(q)):
                node = q.popleft()
                maximum = max(node.val, maximum)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            
            res.append(maximum)
        
        return res