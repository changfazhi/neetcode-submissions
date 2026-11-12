class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        # need to find an value not a boundary
        while lo < hi:
            mid = (lo + hi) // 2
            # check mid with hi
            if nums[mid] > nums[hi]: #min is on the right side
                lo = mid + 1
            else: # this means that nums[mid] <= nums[hi]
                hi = mid # it is = because mid might be correct, we cannot skip it 
        
        return nums[hi]
