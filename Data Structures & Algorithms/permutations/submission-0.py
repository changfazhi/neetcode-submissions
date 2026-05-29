class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case - the length of the path must be the same as the nusm
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            # iterate over the choices
            for i in range(len(nums)):
                # pruning - ensure there is no duplicates
                if nums[i] in path:
                    continue
                
                # make a choice
                path.append(nums[i])
                # explore another choice
                backtrack(path)
                # undo
                path.pop()
        
        backtrack([])
        return res
        