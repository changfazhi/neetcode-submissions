class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        # multi-source expansion bfs 
        q = deque()
        INF = 2147483647
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                # i need to see all the treasures
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        distance = 0 # distance as added as each layer progresses
        while q:
            distance += 1 # introduction of a new layer
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    # need to set condition to ensure it is land and it is not out of bounds
                    if (0 <= nr < ROWS) and (0 <= nc < COLS):
                        if grid[nr][nc] == INF and (nr, nc) not in visited:
                            grid[nr][nc] = distance # in-place modification
                            visited.add((nr,nc))
                            q.append((nr,nc))
