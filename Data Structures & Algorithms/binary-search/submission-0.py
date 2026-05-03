class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(low, high):
            if low > high:
                return -1
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return helper(low, mid - 1)
            else:
                return helper(mid + 1, high)
        return helper(0, len(nums) - 1)
         