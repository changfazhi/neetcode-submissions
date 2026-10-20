class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board) # rows
        m = len(board[0]) # cols

        # i should have a set to keep track of what i have seen
        # row set to track 1 - 9
        # col set to track 1 - 9
        # box set to track 1 - 9 (row / 3) * 3 + (col / 3)

        for i in range(n):
            # create a set to keep track of what i have seen, if it is already in the set then i know there is duplicate
            rowSet = set()
            colSet = set()
            for j in range(m):
                if board[i][j] != "." and board[i][j] not in rowSet:
                    rowSet.add(board[i][j])
                elif board[i][j] != "." and board[i][j] in rowSet:
                    return False
            
                # same logic but for cols
                if board[j][i] != "." and board[j][i] not in colSet:
                    colSet.add(board[j][i])
                elif board[j][i] != '.' and board[j][i] in colSet:
                    return False
        
        # same logic for the 3x3 box
        boxMap = defaultdict(list)
        for i in range(n):
            for j in range(m):
                idx = (i // 3) * 3 + (j // 3) # key
                
                if board[i][j] != "." and board[i][j] not in boxMap[idx]:
                    boxMap[idx].append(board[i][j])
                elif board[i][j] != "." and board[i][j] in boxMap[idx]:
                    return False
                
        
        return True


        