# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        hashMap = {}
        
        while q:
            hashSet = set()
            for i in range(len(q)):
                node = q.popleft()
                hashSet.add(node.val)
                
                if node.right:
                    q.append(node.right)
                    hashMap[node.right.val] = node
                
                if node.left:
                    q.append(node.left)
                    hashMap[node.left.val] = node
                
            if x in hashSet and y in hashSet and hashMap[x] != hashMap[y]:
                return True
        
        return False