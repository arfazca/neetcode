class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        T, B = 0, ROWS-1

        while T <= B:
            M = (B + T) // 2
            if target > matrix[M][-1]:
                T = M + 1
            elif target < matrix[M][0]:
                B = M - 1
            else:
                break

        if not (T<=B):
            return False
        
        M = T + (B - T) // 2
        L, R = 0, COLS-1
        while (L<=R):
            MID = (R + L) // 2
            if target > matrix[M][MID]:
                L = M + 1
            elif target < matrix[M][MID]:
                R = M - 1
            else: 
                return True
        return False