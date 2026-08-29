class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 4

                    if r and grid[r-1][c] == 1:
                        res -= 2
                    if c and grid[r][c-1] == 1:
                        res -= 2
        return res



        