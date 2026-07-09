class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        res = 0
        #area = 0
        # matrix dfs down, each island has their own area then compare the area
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        # write the helper dfs function to find area and paint each coor as visited
        def dfs(r, c):
            # base case - out of bounds, in water, already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS) or (grid[r][c] == 0) or (r,c) in visited:
                return
            
            # paint island as visited
            visited.add((r,c))
            area[0] += 1
            

            directions = ((1,0), (-1,0), (0,1), (0,-1))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # find the start of the island and run dfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = [0]
                    dfs(r,c)
                    res = max(area[0], res)
        
        return res