class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * (n + 1)
        table = []
        for i in range(m):
            table.append(row.copy())
        
        
        
        for col in range(1, n+1):
            table[0][col] = 1
        
        for row in range(1, m):
            for col in range(1, n+1):
                table[row][col] = table[row-1][col] + table[row][col-1]
        
        
        return table[m-1][n]


        
        