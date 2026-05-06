class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(nlogm) time and O(1) space
        # iterate for piles -> binary search
        # lowest bound = len(piles)
        # upper bound = summation of everything in piles, k=1
        
        lowest_k = 1
        highest_k = max(piles)
        
        
        while lowest_k <= highest_k:
            time = 0
            mid = (lowest_k + highest_k) // 2
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)
            
            if time <= h:
                result = mid
                highest_k = mid - 1
            elif time > h:
                lowest_k = mid + 1
        
        return result
        


        