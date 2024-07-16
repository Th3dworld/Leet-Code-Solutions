class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Create set to sort values
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
        