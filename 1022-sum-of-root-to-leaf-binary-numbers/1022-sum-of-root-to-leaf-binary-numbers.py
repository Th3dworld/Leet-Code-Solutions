# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(root, num):
            if not root:
                return
            
            num += str(root.val)
            
            if not root.left and not root.right:
                nums.append(num)
                return
            
            dfs(root.left, num)
            dfs(root.right, num)
        
        dfs(root, "")
        total = 0
        
        
        for i in range(len(nums)):
            val = 0
            j = 0
            num = int(nums[i])
            
            while j < len(nums[i]):
                val += num%10 * pow(2,j)
                num //= 10
                j += 1
            
            total += val
        
        return total
                
            