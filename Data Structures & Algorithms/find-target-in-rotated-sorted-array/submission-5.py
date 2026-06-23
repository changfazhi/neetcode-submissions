class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            # verify - aka base case
            if nums[mid] == target:
                return mid
            # i need to find which part of nums is sorted
            if nums[lo] <= nums[mid]: # this means that the lower portion is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1


            
        