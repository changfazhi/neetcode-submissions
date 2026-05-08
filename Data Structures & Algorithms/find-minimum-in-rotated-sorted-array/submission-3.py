class Solution:
    def findMin(self, nums: List[int]) -> int:
        # need log n time
        n = len(nums)
        low = 0
        high = n - 1
        smallest = nums[0]
        if n == 1:
            return nums[0]

        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] > smallest:
                low = mid + 1
            elif nums[mid] < smallest:
                smallest = nums[mid]
                high = mid - 1
            else:
                low += 1
                continue
        return smallest

        