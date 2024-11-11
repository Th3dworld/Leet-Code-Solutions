# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            minHeap.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        heapq.heapify(minHeap)
        count = 0
        
        while count != k-1:
            heapq.heappop(minHeap)
            count += 1
        
        return heapq.heappop(minHeap)