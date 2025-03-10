class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        
        for i,v in enumerate(nums):
            if target-v in hashSet:
                return [hashSet[target - v], i]
            hashSet[v] = i