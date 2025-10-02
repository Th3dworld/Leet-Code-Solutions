class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False
        
        for i in range(len(matrix)):
            l,r = 0, len(matrix[i]) - 1
            if matrix[i][l] <= target and matrix[i][r] >= target:
                while l <= r:
                    m = l + (r - l)//2
                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
        
        return False