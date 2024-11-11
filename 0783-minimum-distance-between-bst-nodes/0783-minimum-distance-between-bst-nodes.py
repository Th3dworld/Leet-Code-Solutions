# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        nums = []
        minimum = float("inf")
        
        while stack:
            node = stack.pop()
            nums.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                minimum = min(minimum, abs(nums[i] - nums[j]))
        
        return minimum