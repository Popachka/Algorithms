import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def condition(speed) -> bool:
            return sum(math.ceil(pile / speed) for pile in piles) <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
