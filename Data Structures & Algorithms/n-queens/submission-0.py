class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        # keep track of what the queens are threathening
        cols = set()
        pos_dig = set()
        neg_dig = set()
        # helper function to convert into the answer they want based on state
        def board(state):
            res = []
            for col in state:
                row = ["."] * n
                row[col] = "Q"
                row = "".join(row)
                res.append(row)
            return res

        def backtrack(row, state):
            # base case is when every row has a queen
            if row == n:
                res.append(board(state))
            
            # iterate choice, choice is placing queen in every col of the current row we are at
            for col in range(n):
                # pruning - if queen placed in threathened position, we need to skip the current iteration
                if col in cols or (row+col) in pos_dig or (col-row) in neg_dig:
                    continue
                
                # make a choice
                cols.add(col)
                pos_dig.add(row+col)
                neg_dig.add(col-row)
                state.append(col)

                # explore next choice
                backtrack(row+1, state)

                # undo   
                cols.remove(col)
                pos_dig.remove(row+col)
                neg_dig.remove(col-row)
                state.pop()
        
        backtrack(0, [])
        return res
        