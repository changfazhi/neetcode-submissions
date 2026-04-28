class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # time is O(n^2) and space is O(n^2) -> need do nested loop
        # prob need to create new matrix
        # check row if there is duplicate, return false
        n = len(board)
        m = len(board[0])
        for row in board:
            freqMapRow = {}
            for element in row:
                if freqMapRow.get(element) and element != ".":
                    return False
                else:
                    freqMapRow[element] = 1
        
        # check column if there is duplicate
        for i in range(n):
            freqMapCol = {}
            for j in range(m):
                if freqMapCol.get(board[j][i]) and board[j][i] != ".":
                    return False
                else:
                    freqMapCol[board[j][i]] = 1
        
        # check 3x3 sub box to check for duplicate
        freqMapBox = {k: [] for k in range(n)} # create a dict of list, iterate the list to see freq
        for k in range(n): # checking for rows
            for l in range(m): # checking for column
                idx = (k // 3) * 3 + (l // 3)
                freqMapBox[idx].append(board[k][l])
        
        
        for idx in freqMapBox:
            freqMap = {}
            for element in freqMapBox[idx]:
                if freqMap.get(element) and element != ".":
                    return False
                else:
                    freqMap[element] = 1
        
        return True


                 




        