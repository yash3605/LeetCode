class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefixSum = [[0] * n for _ in range(m)]
        self.matrix = matrix

        for i in range(m):
            sum = 0
            for j in range(n):
                sum += matrix[i][j]
                self.prefixSum[i][j] = sum

    def sumRegionBF(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.matrix[i][j]

        return sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                sum += self.prefixSum[i][col2]
            else:
                sum += self.prefixSum[i][col2] - self.prefixSum[i][col1 - 1]
        return sum




matrixSum = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(matrixSum.sumRegion(2, 1, 4, 3)) # returns 8
print(matrixSum.sumRegion(1, 1, 2, 2)) # returns 11
print(matrixSum.sumRegion(1, 2, 2, 4)) # returns 12
