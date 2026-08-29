class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count_rows = [0] * rows
        count_cols = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count_rows[r] += 1
                    count_cols[c] += 1

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (count_rows[r] >1 or count_cols[c] > 1):
                    res += 1

        return res


        
        