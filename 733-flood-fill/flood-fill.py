class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        n = len(image)
        m = len(image[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= n or c <0 or c >= m or (r,c) in visited or image[r][c] != original_color:
                return 
            visited.add((r,c))
            image[r][c] = color

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)


        for r in range(n):
            for c in range(m):
                if r == sr and c == sc:
                    dfs(r,c)
        return image

        
        