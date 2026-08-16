class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid2)
        cols = len(grid2[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        ans = 0

        def dfs(r, c):
            # Invalid
            if not (0 <= r < rows and 0 <= c < cols):
                return True

            # Water or already visited
            if grid2[r][c] == 0 or (r, c) in visit:
                return True

            visit.add((r, c))

            # Current cell must also be land in grid1
            valid = grid1[r][c] == 1

            # Check all neighbors
            for dr, dc in dirs:
                valid = dfs(r + dr, c + dc) and valid

            return valid


        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r,c) not in visit:
                    if dfs(r,c):
                        ans += 1
        return ans


        