class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(1) space
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            # if valid
            if nums[mid] == target:
                return mid
            # if too low
            elif nums[mid] < target:
                # shift up the mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        
        return -1
        