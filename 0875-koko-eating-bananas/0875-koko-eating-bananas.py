class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minimum = float("inf")

        while l <= r:
            m = (l + r)//2
            count = 0

            for n in piles:
                hrs = 1
                while n > m * hrs:
                    hrs += 1
                count += hrs
            minimum = min(count, minimum)

            
            l = m + 1

        return minimum
