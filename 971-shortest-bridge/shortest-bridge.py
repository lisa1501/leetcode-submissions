class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque([])
        found = False

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 

            grid[r][c] = 2
            q.append((r, c))

            for dr, dc in dirs:
                dfs(dr + r, dc + c)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    found = True
                    dfs(r, c)
                    break

            if found == True:
                break
            
        distance = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r+dr 
                    nc = c+dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            return distance

                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            distance += 1
        