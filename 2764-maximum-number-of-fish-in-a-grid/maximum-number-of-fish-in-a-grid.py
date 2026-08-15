class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col):
            fish = 0
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] != 0:
                fish += grid[row][col] 
                grid[row][col] = 0
                for dr, dc in dirs:
                    fish += dfs(row+dr, col+dc)

            return fish

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    ans = max(ans, dfs(r,c)) 
                    
        return ans
        