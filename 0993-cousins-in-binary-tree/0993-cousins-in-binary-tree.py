# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        
        while q:
            hashMap = {}
            for i in range(len(q)):
                node = q.popleft()
                
                if node.right:
                    q.append(node.right)
                    hashMap[node.right.val] = node.val
                    
                if node.left:
                    q.append(node.left)
                    hashMap[node.left.val] = node.val
            
            print(hashMap)
            if x in hashMap and y in hashMap and hashMap[x] != hashMap[y]:
                    return True
                
        return False