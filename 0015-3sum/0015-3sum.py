class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            
            if v > 0:
                break
            
            l,r = i + 1, len(nums) - 1

            while l < r:
                total = v + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res
