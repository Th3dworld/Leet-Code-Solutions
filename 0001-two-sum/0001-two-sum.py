class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = dict()
        for i in range(len(nums)):
            if value_to_index.get(target - nums[i]) is not None:
                return [value_to_index[target - nums[i]], i]
            value_to_index[nums[i]] = i
        return []