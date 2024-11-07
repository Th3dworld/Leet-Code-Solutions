# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        q = deque([root])
        Map = dict()
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val == val:
                    return node
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return None