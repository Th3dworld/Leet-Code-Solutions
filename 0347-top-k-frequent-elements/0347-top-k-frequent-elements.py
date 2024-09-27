class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n,0) + 1
        
        for n, occ in count.items():
            res[occ].append(n)
        
        output = []
        
        for i in range(len(nums),-1,-1):
            for v in res[i]:
                output.append(v)
                if len(output) == k:
                    return output
    
                
        
            
        
        
        
        