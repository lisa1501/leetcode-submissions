class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefix_matrix[r][c + 1]
                self.prefix_matrix [r + 1][c + 1] = prefix + above

        # print(self.prefix_matrix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.prefix_matrix[row2][col2]
        above = self.prefix_matrix [row1 - 1][col2]
        left = self.prefix_matrix [row2][col1 - 1]
        topLeft = self.prefix_matrix [row1 - 1][col1 - 1]
        print(self.prefix_matrix[row2][col2],self.prefix_matrix [row1 - 1][col2], self.prefix_matrix [row2][col1 - 1],self.prefix_matrix [row1 - 1][col1 - 1])
        return bottomRight - above - left + topLeft

    
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)