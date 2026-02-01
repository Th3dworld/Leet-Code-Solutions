class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        
        for index, value in enumerate(nums):
            if target - value in Map:
                return [Map[target-value], index]
            Map[value] = index
        
        return []
        