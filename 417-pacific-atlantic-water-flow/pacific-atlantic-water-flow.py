class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        pacific = set()
        atlantic = set()

        def dfs(r, c , visited):
            visited.add((r,c))
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if not (0<=nr<rows and 0<=nc<cols):
                    continue

                if (nr,nc) in visited:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(rows-1, c, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


        

        