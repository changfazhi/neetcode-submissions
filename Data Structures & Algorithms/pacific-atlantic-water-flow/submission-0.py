class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        # looks like a matrix dfs kind of problem
        res = []
        pacific, athlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        # i am adding the coordinates of the points to the res
        # dfs helper
        def dfs(r,c,visited, prevHeight):
            # base case
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or prevHeight > heights[r][c] or (r,c) in visited:
                return
            
            # add into visited
            visited.add((r,c))

            # check neighbour
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # i need to call dfs
        # i need to call them from the border
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, athlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, athlantic, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in athlantic and (r,c) in pacific:
                    res.append([r,c])

        
        
        return res


