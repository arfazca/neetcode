class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L, R = 0, len(matrix)-1

        while L < R:
            for i in range(L, R+1):
                T, B = L, R
                S = matrix[T][L+i]
                matrix[T][L+i] = matrix[B-i][L]
                matrix[B-i][L] = matrix[B][R-i]
                matrix[B][R-i] = matrix[T+i][R]
                matrix[T+i][R] = S
            L, R = L+1, R-1