class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet1 = set(nums1)
        hashSet2 = set(nums2)
        res = set()
        
        for num in nums1:
            if num in hashSet1 and num in hashSet2:
                res.add(num)
        
        return list(res)