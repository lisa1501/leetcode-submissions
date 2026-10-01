class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid2)
        cols = len(grid2[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        ans = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return

            grid2[r][c] = 0

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and grid1[r][c] == 0:
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    dfs(r, c)
                    ans += 1
        return ans