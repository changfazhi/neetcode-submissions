class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) time and constant space -> must use state variables
        # i am able to use nested loops
        # have 2 pointers, then use compliment to find if it is possible to achieve 0
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            target = -nums[i] # -nums[i] = nums[left] + nums[right]
            for j in range(n - i - 1):
                if left >= right:
                    break
                elif nums[left] + nums[right] == target:
                    if [-target, nums[left], nums[right]] in res:
                        break
                    else:
                        res.append([-target, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                
        
        return res


