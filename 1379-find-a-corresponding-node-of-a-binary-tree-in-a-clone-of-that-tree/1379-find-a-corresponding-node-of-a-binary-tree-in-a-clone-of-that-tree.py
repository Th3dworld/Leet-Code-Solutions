# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        print(target)
        
        q = deque([original])
        clone = deque([cloned])
        
        while q:
            node = q.popleft()
            clonode = clone.popleft()
            
            if node.val == target.val and clonode.val == target.val:
                return clonode
            
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
                
            if clonode.right:
                clone.append(clonode.right)
            if clonode.left:
                clone.append(clonode.left)
            
        return None