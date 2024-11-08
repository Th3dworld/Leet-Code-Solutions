# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        
        while q:
            total = 0
            length = len(q)
            for i in range(len(q)):
                node = q.popleft()
                total += node.val
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            
            res.append(total/length)
            
        return res 