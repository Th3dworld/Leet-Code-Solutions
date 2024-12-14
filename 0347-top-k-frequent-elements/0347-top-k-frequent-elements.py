class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize variables
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        res = []
        
        #Solve problem
        for val, occ in count.items():
            bucket[occ].append(val)
        
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                
                if len(res) == k:
                    return res
        