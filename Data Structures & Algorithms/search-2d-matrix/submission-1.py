class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        # need to convert 2d array into 1d array
        # i can do nested for loops, but that wouldnt satisify time requirements
        # index = (row * n) + col

        # maybe i can convert 1d into 2d array
        # row = index // n
        # cols = index % n
        lo, hi = 0, (n * m) - 1
        while lo <= hi: # i want to be able to find the exact
            # convert them into 2d, and make mid the index since that is sant i am trying to find anyways.
            # conver the rows, cols to fit into 2d (i had to refer to the my anki deck to remember how to convert rows and cols into 2d from 1d)
            mid = (lo + hi) // 2
            row, col = (mid // n), (mid % n)
            if target == matrix[row][col]:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False