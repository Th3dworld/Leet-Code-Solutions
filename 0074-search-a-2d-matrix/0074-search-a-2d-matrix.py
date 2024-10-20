class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for n in matrix:
            if n[len(n)-1] < target:
                continue
                
            l,r = 0, len(n)-1
            
            while l <= r:
                m = (l+r)//2
                
                if n[m] > target:
                    r = m-1
                elif n[m] < target:
                    l = m + 1
                else:
                    return True
        return False
                