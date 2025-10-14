class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        hours = r

        while l <= r:
            k = l + (r - l)//2
            time = 0
            for p in piles:
                time += math.ceil(float(p)/k)

            if time <= h:
                hours = min(hours, k)
                r = k - 1
            else:
                l = k + 1

        return hours
