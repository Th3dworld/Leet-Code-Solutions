class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix),len(matrix[0])
        
        top,bot = 0,ROW-1
        while top <= bot:
            row = (top+bot)//2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not (top<=bot): return False
        row = (top+bot)//2
        l,r = 0,COL-1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] > target:
                r = m-1
            elif matrix[row][m] < target:
                l = m+1
            else:
                return True
        return False
        
#         ROWS, COLS = len(matrix), len(matrix[0])

#         top, bot = 0, ROWS - 1
#         while top <= bot:
#             row = (top + bot) // 2
#             if target > matrix[row][-1]:
#                 top = row + 1
#             elif target < matrix[row][0]:
#                 bot = row - 1
#             else:
#                 break

#         if not (top <= bot):
#             return False
#         row = (top + bot) // 2
#         l, r = 0, COLS - 1
#         while l <= r:
#             m = (l + r) // 2
#             if target > matrix[row][m]:
#                 l = m + 1
#             elif target < matrix[row][m]:
#                 r = m - 1
#             else:
#                 return True
#         return False