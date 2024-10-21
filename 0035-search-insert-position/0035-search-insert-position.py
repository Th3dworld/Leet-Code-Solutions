class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        res = 0
        while l<=r:
            m = (l + r) // 2
            if nums[m] > target:
                if nums[m - 1] < target: 
                      res = m
                r = m - 1
            elif nums[m] < target:
                if nums[m] < target and (m == len(nums)-1 or nums[m + 1] > target): 
                      res = m+1
                l = m + 1
            else:
                return m
        return res