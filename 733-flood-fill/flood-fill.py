class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        rows = len(image)
        cols = len(image[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return 

            image[r][c] = color
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                dfs(nr, nc)



        for r in range(rows):
            for c in range(cols):
                if r == sr and c == sc:
                    dfs(r, c)
        return image


        