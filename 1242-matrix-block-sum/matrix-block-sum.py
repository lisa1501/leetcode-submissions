class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        prefix_mat = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for r in range(rows):
            for c in range(cols):
                prefix_mat[r+1][c+1] = mat[r][c] + prefix_mat[r][c+1] + prefix_mat[r+1][c] - prefix_mat[r][c]

        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                r1 = max(0, r-k)
                c1 = max(0, c-k)
                r2 = min(rows-1, r+k)
                c2 = min(cols-1, c+k)

                ans[r][c] = prefix_mat[r2+1][c2+1] - prefix_mat[r2+1][c1] - prefix_mat[r1][c2+1] + prefix_mat[r1][c1]

        return ans


        