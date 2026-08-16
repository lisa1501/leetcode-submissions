class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        

        def islandsNum():
            visited = set()
            def dfs(r, c):
                if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c]==0:
                    return 

                visited.add((r,c))

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                    dfs(nr, nc)

            islands_num = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        islands_num += 1
                        dfs(r,c)
                        
            return islands_num

        if islandsNum() != 1:
            return 0

        for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        grid[r][c] = 0
                    # After removing one land cell, did the island become disconnected?
                        if islandsNum() != 1:
                            return 1

                        grid[r][c] = 1
        return 2





        

            

        