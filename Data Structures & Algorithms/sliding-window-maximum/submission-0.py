class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        window = nums[:k]
        max_window = max(window)
        res.append(max_window)

        for right in range(k, len(nums)):
            left += 1
            window_frame = nums[left:right+1]
            max_window_frame = max(window_frame)
            res.append(max_window_frame)
        
        return res