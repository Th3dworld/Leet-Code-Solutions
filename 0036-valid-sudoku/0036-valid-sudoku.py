class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = collections.defaultdict(set)
        COLS = collections.defaultdict(set)
        GRID = collections.defaultdict(set)

        for ROW in range(len(board)):
            for COL in range(len(board)):
                if board[ROW][COL] == ".":
                    continue
                elif board[ROW][COL] in ROWS[ROW]:
                    return False
                elif board[ROW][COL] in COLS[COL]:
                    return False
                elif board[ROW][COL] in GRID[(ROW//3,COL//3)]:
                    return False
                else:
                    GRID[(ROW//3,COL//3)].add(board[ROW][COL])
                    COLS[COL].add(board[ROW][COL])
                    ROWS[ROW].add(board[ROW][COL])
        
        return True