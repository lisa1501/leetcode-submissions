class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return 

            board[r][c] = "Y"

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        for r in range(rows):
            for c in [0, cols-1]:
                dfs(r, c)

        for c in range(cols):
            for r in [0, rows-1]:
                dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "Y":
                    board[r][c] = "O"

        return board


        