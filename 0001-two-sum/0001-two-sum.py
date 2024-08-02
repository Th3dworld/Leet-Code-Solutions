class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToindex = dict()
        for i in range(len(nums)):
            if(valueToindex.get(target - nums[i], -1) != -1):
                return[i, valueToindex[target - nums[i]]]
            valueToindex[nums[i]] = i
        return []
        