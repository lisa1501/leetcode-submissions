class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        island_id = 2
        area = {}

        def dfs(r, c, idx):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            grid[r][c] = idx
            size = 1

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                size += dfs(nr, nc,idx)

            return size

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area[island_id] = dfs(r,c,island_id)
                    island_id += 1
                        

        if len(area) == 0:
            return 1
        ans = max(area.values())       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    total = 1
                    seen = set()
                    for dr, dc in dirs:
                        nr = dr + r
                        nc = dc + c
                        if 0 <= nr < rows and 0 <= nc < cols:
                            nei_id = grid[nr][nc]

                            if nei_id not in seen:
                                seen.add(nei_id)
                                total += area.get(nei_id, 0)

                    ans = max(ans, total)
        return ans

                        

        