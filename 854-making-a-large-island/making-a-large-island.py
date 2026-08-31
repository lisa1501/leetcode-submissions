class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        ans = 0
        islandId_to_size = {}
        islandId = 2

        def dfs(r, c, num):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            grid[r][c] = num
            size = 1

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                size += dfs(nr, nc, num)

            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    islandId_to_size[islandId] = dfs(r, c, islandId)
                    islandId += 1

        if len(islandId_to_size) == 0:
            return 1
        ans = max(islandId_to_size.values())

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    total = 1
                    seen = set()

                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc

                        if 0<=nr<rows and 0<=nc<cols:
                            nei_id = grid[nr][nc]

                            if nei_id not in seen:
                                seen.add(nei_id)
                                total += islandId_to_size.get(nei_id,0)

                    ans = max(ans, total)

        return ans