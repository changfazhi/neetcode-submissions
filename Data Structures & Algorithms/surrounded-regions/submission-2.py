class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        ROWS, COLS = len(board), len(board[0])
        q = deque([])
        # prob can just use matrix bfs, multi-source expansion
        # seeding - i need to check the neighbour and ensure 2 things
        # 1. it is not OOB
        # 2. the neighbour has at least 1 '0'

        # seeding all the border 
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r,0))
                visited.add((r,0))
                board[r][0] = "#"

            if board[r][COLS-1] == "O":
                q.append((r, COLS-1))
                visited.add((r, COLS-1))
                board[r][COLS-1] = "#"
        
        for c in range(COLS):
            if (0, c) is not visited and board[0][c] == "O":
                q.append((0, c))
                visited.add((0,c))
                board[0][c] = "#"

            if (ROWS-1, c) is not visited and board[ROWS-1][c] == "O":
                q.append((ROWS-1, c))
                visited.add((ROWS-1, c))
                board[ROWS-1][c] = "#"
        

        # multi-source expansion to change all borders to #
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "O" and (row, col) not in visited:
                        board[row][col] = "#"
                        q.append((row, col))
                        visited.add((row, col))
        

        # second pass, change remaining 0 to X and the # to 0. The order matters here
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

        #return board

        
        