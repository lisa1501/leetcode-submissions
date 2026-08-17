class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c))

        if len(q) == 0 or len(q) == rows*rows:
            return -1

        distance = -1

        while q:
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr <rows and 0 <= nc <cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))  
            
        return distance
