class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
            
            m = l + (r - l)//2
            res = min(res, nums[m])
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res