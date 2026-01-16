class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index,value in enumerate(nums):
            if target - value in hashMap:
                return [hashMap[target - value], index]
            hashMap[value] = index
        
        return []