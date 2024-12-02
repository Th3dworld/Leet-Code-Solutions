class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        numsSet = set(nums)
        rangeEnd = nums[-1]
        res = []
        
        for num in nums:
            hold=""
            length = 0
            
            if num - 1 not in numsSet:
                hold += str(num)
                
                while num + length in numsSet:
                    length += 1
                    
                length -= 1
            
            if length != 0:
                hold += "->"
                hold += str(num + length)
            
            if hold != "":
                res.append(hold)
            
        
        return res
                