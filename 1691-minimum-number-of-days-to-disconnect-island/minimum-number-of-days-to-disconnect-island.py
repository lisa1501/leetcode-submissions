class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def islandsNum():
            visited = set()
            def dfs(r,c):
                if r < 0 or r >= rows or c <0 or c>=cols or grid[r][c]==0 or (r,c) in visited:
                    return 

                visited.add((r,c))

                for dr, dc in dirs:
                    dfs(r+dr, c+dc)
                    
            res = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        dfs(r,c)
                        res += 1
            return res

        if islandsNum() != 1:
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if islandsNum() != 1:
                        return 1
                    grid[r][c] = 1
        return 2

                    
                    


        