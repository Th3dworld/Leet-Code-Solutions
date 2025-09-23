class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        l,r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r -= 1
            if nums[mid] < target:
                l += 1
        
        return -1