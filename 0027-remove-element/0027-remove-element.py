class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] != val:
                k += 1
                l += 1
            elif nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:

                r -= 1

        
        return k