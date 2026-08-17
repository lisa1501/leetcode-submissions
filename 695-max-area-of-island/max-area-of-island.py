class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or (r,c) in visited:
                return 0

            visited.add((r,c))
            size = 1

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                size += dfs(nr, nc)
            return size


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c))
    
        return max_area