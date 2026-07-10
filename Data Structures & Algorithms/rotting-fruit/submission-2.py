class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        # this is a multi-scource BFS, the rotton food should be seeded
        q = deque()
        visited = set()
        # this is to seed all the rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        # now we need to expand from the rotten fruit
        while q:
            
            for _ in range(len(q)):
                r, c = q.popleft()
                # now i need to expand 
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    # now the problem is that idk how to return -1 early if there is no way to spread to fresh fruits
                    # if i do OOB check + check that all is not 1 and return -1 i am missing the case where i actually spread finish already then return -1
                    # the only way i can think of is that one check 4 direction with no fresh fruit and the grid still have fresh fruit
                    # nvm the solution would be to count all the fresh oranges, minus them when the rotten spread
                    # i need to check it is within the grid, ensure i am finding fresh fruits and that i have not already visited the fruit already
                    if (0 <= nr < ROWS) and (0 <= nc < COLS):
                        if grid[nr][nc] == 1 and (nr,nc) not in visited:
                            grid[nr][nc] = 2
                            fresh -= 1
                            q.append((nr,nc))
                            visited.add((nr,nc))
            if q:
                # as it expands, the minute shld increment to show that it takes 1 minute to expand 1 layer
                minute += 1

        return minute if fresh == 0 else -1
        