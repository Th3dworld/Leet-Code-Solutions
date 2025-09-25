class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r =0, len(nums)-1
        Min = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                Min = min(nums[l], Min)
            
            m = l + (r - l)//2
            Min = min(nums[m], Min)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return Min