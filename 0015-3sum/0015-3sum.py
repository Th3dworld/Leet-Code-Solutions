class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i,v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            if v > 0:
                break
            
            l,r = i + 1, len(nums) - 1

            while l < r:
                if v + nums[l] + nums[r] > 0:
                    r -= 1
                elif v + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res