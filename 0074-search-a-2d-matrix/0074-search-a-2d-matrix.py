class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False
        
        for i in range(len(matrix)):
            l,r = 0, len(matrix[0])-1
            if target >= matrix[i][0] and target <= matrix[i][r]:
                while l <= r:
                    mid = l + (r - l)//2
                    if target == matrix[i][mid]:
                        return True
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    elif matrix[i][mid] < target:
                        l = mid + 1
        
        return False
                        