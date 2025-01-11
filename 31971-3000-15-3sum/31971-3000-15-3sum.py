class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for p in range(len(nums)-2):
            if p > 0 and nums[p] - nums[p-1] == 0:
                continue
                
            l,r = p+1, len(nums)-1
            
            while l < r:
                if nums[p] + nums[r] + nums[l] > 0:
                    r -= 1
                elif nums[p] + nums[r] + nums[l] < 0:
                    l += 1
                else:
                    res.append([nums[p], nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                
                    