class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, path):
            # base case: if valid , in this case anything is valid
            res.append(list(path))
            # iterate over the choices
            for i in range(idx, len(nums)):
                # check constraints (pruning)
                # no constraints
                # make a choice
                path.append(nums[i])
                # explore the choice - move to the next step with updated state
                backtrack(i + 1, path)
                # undo the choice
                path.pop()
            
        
        backtrack(0, [])
        return res
