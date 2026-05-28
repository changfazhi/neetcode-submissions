class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if idx >= len(nums) or total > target:
                return
            
            # include the nums[idx]
            path.append(nums[idx])
            backtrack(idx, path, total + nums[idx])
            path.pop()

            # dont include nums[idx]
            backtrack(idx+1, path, total)
        
        backtrack(0, [], 0)
        return res

            
        