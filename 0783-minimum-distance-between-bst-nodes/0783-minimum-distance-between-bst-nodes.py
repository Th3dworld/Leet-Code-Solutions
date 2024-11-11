# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root, arr):
            if not root:
                return
            
            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)
        nums = []
        dfs(root, nums)
        
        low = float("inf")
        
        for i in range(len(nums)-1):
            low = min(low, abs(nums[i] - nums[i+1]))
        
        return low
        