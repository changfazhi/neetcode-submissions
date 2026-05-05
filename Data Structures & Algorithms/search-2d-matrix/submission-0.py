class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using binary search method to half row first
        # then same method for col
        # then try find like that
        row = len(matrix)
        col = len(matrix[0])

        # tryna find the row where target resides
        top, bot = 0, row - 1
        while top <= bot:
            mid1 = (top + bot) // 2
            if matrix[mid1][0] <= target <= matrix[mid1][-1]:
                row = mid1
                break
            elif target < matrix[mid1][0]:
                bot = mid1 - 1
            elif target > matrix[mid1][-1]:
                top = mid1 + 1
        if not (top <= bot):
            return False
        left, right = 0, col - 1
        while left <= right:
            mid2 = (left + right) // 2
            if target == matrix[row][mid2]:
                return True
            elif target < matrix[row][mid2]:
                right = mid2 - 1
            elif target > matrix[row][mid2]:
                left = mid2 + 1
        return False

        
