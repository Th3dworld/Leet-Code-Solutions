class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minimum = float("inf")
        m = 0

        while l <= r:
            m = (l + r)//2
            count = 0

            for n in piles:
                count += math.ceil(float(n)/m)
            if count <= h:
                minimum = min(m, minimum)
                r = m - 1
            else:
                l = m + 1
            
        return minimum

      
