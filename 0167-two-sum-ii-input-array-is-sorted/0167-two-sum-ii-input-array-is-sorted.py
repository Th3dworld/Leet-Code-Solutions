class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        valueToIndex = {}
        
        for i,v in enumerate(numbers):
            if target - v in valueToIndex:
                return [valueToIndex[target - v], i + 1]
            valueToIndex[v] = i + 1
        
        return []