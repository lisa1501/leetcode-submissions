class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 0:
                return 

            grid[r][c] = 1

            for dr, dc in dirs:
                dfs(dr+r, dc+c)


        for r in range(rows):
            for c in [0, cols-1]:
                dfs(r, c)

        for c in range(cols):
            for r in [0, rows-1]:
                dfs(r, c)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    res += 1
                    dfs(r,c)
        return res

                
                
        