class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                dummy = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = dummy


        for i in matrix:
            i.reverse()
