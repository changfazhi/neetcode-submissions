class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # base case: the num in path must equate to target
        def backtrack(idx, path, total):
            if total == target:
                res.append(path[:])
                return
            # pruning
            if total > target:
                return
            # iterate the choices
            for i in range(idx, len(candidates)):
                # pruning - if loop move forward and sees a duplicate, it skips it
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                # make choice
                path.append(candidates[i])
                # explore - move on with the index since each element in the list is only chosen ONCE
                backtrack(i + 1, path, total + candidates[i])
                # undo
                path.pop()
        
        backtrack(0, [], 0)
        return res

        