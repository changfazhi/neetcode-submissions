class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, path, total):
            # base case is when all the el in the path equal to target, so i should have it track total such that total = target means i can return 
            if total == target:
                res.append(path[:])
                return
            # pruning incase total goes too far
            if total > target:
                    return
            # iterate over the choice
            for i in range(idx, len(nums)):
                # make a choice
                path.append(nums[i])
                # explore 1 - since i can use repeated nums[i], i does not change
                backtrack(i, path, total + nums[i])
                # undo
                path.pop()
                
        
        backtrack(0,[],0)
        return res