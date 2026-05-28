class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, path):
            if idx == len(nums):
                res.append(path[:])
                return
            
            # include nums[idx]
            path.append(nums[idx])
            backtrack(idx+1, path)
            path.pop()

            # dont include nums[idx]
            backtrack(idx+1, path)
        backtrack(0, [])
        return res

        