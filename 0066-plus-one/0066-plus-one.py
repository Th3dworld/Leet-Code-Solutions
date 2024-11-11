class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        res = []
        
        for i in range(len(digits)):
            num += digits[i]
            if i != len(digits)-1:
                num *= 10
        
        num += 1
        num = str(num)
        
        for i in num:
            res.append(int(i))
        
        return res