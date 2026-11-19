class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or (r,c) in visited or grid[r][c] != 1:
                return 0

            visited.add((r,c))
            island_area = 1

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                island_area += dfs(nr, nc)
                
            return island_area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, dfs(i,j))

        return max_area
        