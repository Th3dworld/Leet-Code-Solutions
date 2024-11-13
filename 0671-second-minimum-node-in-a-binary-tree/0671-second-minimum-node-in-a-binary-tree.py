# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        hashSet = set()
        def dfs(root):
            if not root:
                return
            
            hashSet.add(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        minHeap = list(hashSet)
        
        heapq.heapify(minHeap)
        heapq.heappop(minHeap)
        
        if minHeap: 
            return heapq.heappop(minHeap)
        else:
            return -1
        
        
        
        