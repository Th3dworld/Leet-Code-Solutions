class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ROW in range(len(matrix)):
            l,r = 0, len(matrix[ROW]) - 1
            if matrix[ROW][l] > target or matrix[ROW][r] < target:
                continue
            while l <= r:
                m = l + (r - l)//2
                if matrix[ROW][m] == target:
                    return True
                elif matrix[ROW][m] < target:
                    l = m + 1
                else:
                    r = m - 1
        
        return False