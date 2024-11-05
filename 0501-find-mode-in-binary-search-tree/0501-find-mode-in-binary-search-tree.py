# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        
        q = deque([root])
        hashMap = {}
        res = []
        maxi = 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val in hashMap:
                    hashMap[node.val] += 1
                    maxi = max(maxi, hashMap[node.val])
                else:
                    hashMap[node.val] = 1
                    maxi = max(maxi, hashMap[node.val])
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        print(hashMap)
        for k,v in hashMap.items():
            if v == maxi:
                res.append(k)
            
        return res
        
        
        