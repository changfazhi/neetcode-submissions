class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # matrix dfs, start dfs at the start of an island
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # base case - out of bounds, in water or already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS) or (grid[r][c] == "0") or ((r,c) in visited):
                return
            # add to hash set to ensure i dont come back to it
            visited.add((r,c))

            # all possible directions in the current position
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                # call itself but move in any of the 4 directions
                dfs(r + dr, c + dc)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                # if i touch land i will call dfs to traverse and paint the rest of the island as visited
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    count += 1
                
        return count


