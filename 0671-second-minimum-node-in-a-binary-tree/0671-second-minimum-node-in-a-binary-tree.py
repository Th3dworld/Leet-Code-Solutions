# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        nums = set()
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                nums.add(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                    
        nums = list(nums)
        
        if len(nums) < 2:
            return -1
        
        heap = nums
        heapq.heapify(heap)
        heapq.heappop(heap)
        
        return heapq.heappop(heap)