class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #use dict
        count = dict()
        for i in nums:
            if count.get(i,0) > 0:
                return True
            count[i] = count.get(i,0) + 1
        return False
    
