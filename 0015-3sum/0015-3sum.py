class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + v
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], v])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return res


