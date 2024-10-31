class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, cum):
            if index >= len(nums):
                res.append(cum[:])
                return
            
            cum.append(nums[index])
            backtrack(index + 1, cum)
            cum.pop()
            backtrack(index + 1, cum)
        backtrack(0,[])
        return res
            