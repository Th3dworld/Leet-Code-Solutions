class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        hashSet1 = set(nums1)
        hashSet2 = set(nums2)
        res = []
        
        for num in nums1:
            if num in hashSet1 and num in hashSet2:
                if count1[num] < count2[num]:
                    length = count1[num]
                    count1[num] -= 1
                else:
                    length = count2[num]
                    count2[num] -= 1
                
                if length > 0:
                    res.append(num)
        
        return res