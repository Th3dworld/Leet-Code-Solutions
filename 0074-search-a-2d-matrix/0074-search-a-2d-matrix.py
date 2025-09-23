class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False
        
        for i in range(len(matrix)):
            l,r = 0, len(matrix[i]) - 1
            if target <= matrix[i][r] and target >= matrix[i][l]:  
                while l <= r:
                    mid = l + (r - l)//2
                    if target == matrix[i][mid]:
                        return True
                    elif target > matrix[i][mid]:
                        l = mid + 1
                    elif target < matrix[i][mid]:
                        r = mid - 1

        return False
                    
                    