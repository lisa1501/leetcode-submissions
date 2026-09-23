class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols =len(matrix[0])

        self.prefix_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefix_matrix[r][c + 1]
                self.prefix_matrix [r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        bottomRight = self.prefix_matrix[row2+1][col2+1]
        topRight = self.prefix_matrix [row1][col2+1]
        bottomleft = self.prefix_matrix [row2+1][col1]
        topLeft = self.prefix_matrix [row1][col1]

        return bottomRight - topRight - bottomleft + topLeft

    
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)