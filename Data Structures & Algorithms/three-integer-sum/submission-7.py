class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O (n^2) time and O(1) extra space
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            # this is to skip the anchor
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
                
            
        return res