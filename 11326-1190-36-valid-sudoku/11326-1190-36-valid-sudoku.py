class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COL = defaultdict(set)
        ROW = defaultdict(set)        
        GRID = defaultdict(set)
        
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in COL[col]:
                    return False
                elif board[row][col] in ROW[row]:
                    return False
                elif board[row][col] in GRID[(row//3, col//3)]:
                    return False
                else:
                    COL[col].add(board[row][col])
                    ROW[row].add(board[row][col])
                    GRID[(row//3, col//3)].add(board[row][col])
        
        return True
            