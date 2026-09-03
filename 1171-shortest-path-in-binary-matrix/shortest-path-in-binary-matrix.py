class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = set()
        visited.add((0,0))
        q = deque([(0,0,1)])
        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),           (0,1),
                (1,-1),  (1,0),   (1,1)]

        while q:
            for _ in range(len(q)):
                r, c, steps = q.popleft()
                 
                if r == n - 1 and c == n - 1:
                    return steps

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, steps+1))

        return -1
        
        