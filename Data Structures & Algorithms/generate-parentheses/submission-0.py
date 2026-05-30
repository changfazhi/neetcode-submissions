class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        params = "()"
        def backtrack(open_count, close_count, path):
            # base case is that the length of path must be twice of that of n
            if len(path) == n*2:
                res.append(path)
                return
            
            # pruning to ensure the number of open bracket is equal to n
            if open_count < n:
                # make the choice
                backtrack(open_count + 1, close_count, path + "(")

            # pruning to ensure each open bracket is closed
            if close_count < open_count:
                # make the choice
                backtrack(open_count, close_count + 1, path + ")")
            

        backtrack(0,0, "")
        return res