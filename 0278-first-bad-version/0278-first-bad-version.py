# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        res = n
        
        while l<=r:
            m = (l + r) // 2
            
            if isBadVersion(m):
                res = min(m,res)
                r = m-1
            else:
                l = m + 1
        return res