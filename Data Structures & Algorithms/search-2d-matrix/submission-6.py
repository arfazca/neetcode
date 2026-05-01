class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T, B = 0, len(matrix)-1
        while (T<=B):
            MM = T + ((B-T)//2)
            if (target > matrix[MM][-1]): T = MM + 1
            elif (target < matrix[MM][0]): B = MM - 1
            else: break
        if not (T<=B): return False
        MM = T + ((B-T)//2)

        L, R = 0, len(matrix[MM])-1
        while (L<=R):
            M = L + ((R-L)//2)
            if (target > matrix[MM][M]): L = M + 1
            elif (target < matrix[MM][M]): R = M - 1
            else: return True
        return False