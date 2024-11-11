class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prevMap = {}
        
        for i,v in enumerate(nums):
            if v in prevMap:
                if abs(i - prevMap[v]) <= k:
                    return True
            prevMap[v] = i
        
        return False