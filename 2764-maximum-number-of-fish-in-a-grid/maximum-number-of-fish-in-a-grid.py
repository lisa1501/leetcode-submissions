class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
                
            fish = grid[r][c]
            visited.add((r,c))

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                fish += dfs(nr, nc)

            return fish

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r,c) not in visited:
                    ans = max(ans, dfs(r,c)) 
                    
        return ans
        