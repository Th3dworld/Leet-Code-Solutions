# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        minHeap = []
        heapq.heapify(minHeap)
        q = deque([root])
        
        print(q)
        
        while q:
            node = q.popleft()
            heapq.heappush(minHeap, node.val)
            
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        
        print(minHeap)
        root = TreeNode()
        curr = root
        
        while minHeap:
            curr.val = heapq.heappop(minHeap)
            if minHeap:
                curr.right = TreeNode()
                curr = curr.right
        
        return root