class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(penis):
            # must return true or false
            count = 0
            for pile in piles:
                # need to round up
                count -= (pile // -penis)
 
            return count <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return hi
        