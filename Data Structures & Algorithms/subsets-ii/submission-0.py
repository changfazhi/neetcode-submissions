class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(idx, path):
            # base case: if path not res can alrdy
            if path not in res:
                res.append(path[:])
                
            # pruning

            # iterate over the choice
            for i in range(idx, len(nums)):
                # pruning
                # make choice
                path.append(nums[i])
                # explore other choice
                backtrack(i+1, path)
                # undo
                path.pop()
        
        backtrack(0, [])
        return res
        