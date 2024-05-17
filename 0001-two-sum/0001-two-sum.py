class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ValueToIndex = dict()
        for index in range(len(nums)):
            if ValueToIndex.get(target - nums[index]) is not None:
                return [ValueToIndex[target - nums[index]], index]
            ValueToIndex[nums[index]] = index
        return []