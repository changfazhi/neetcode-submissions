class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def backtrack(r, c, word_idx):
            # base case is when the length is the same
            if word_idx == len(word):
                return True

            # pruning - edge cases
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[word_idx]):
                return False
            
            # iterate over the choice
            # making choice
            temp = board[r][c]
            board[r][c] = "#"

            # exploring choice
            found = (
                backtrack(r + 1, c, word_idx + 1) or
                backtrack(r, c + 1, word_idx + 1) or
                backtrack(r - 1, c, word_idx + 1) or
                backtrack(r, c - 1, word_idx + 1)
            )
            
            # undo choice
            board[r][c] = temp

            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        
        return False


