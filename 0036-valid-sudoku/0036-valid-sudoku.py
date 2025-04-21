class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = collections.defaultdict(set)
        COLS = collections.defaultdict(set)
        GRIDS = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in ROWS[row]:
                    return False
                elif board[row][col] in COLS[col]:
                    return False
                elif board[row][col] in GRIDS[(row//3,col//3)]:
                    return False
                else:
                    GRIDS[(row//3, col//3)].add(board[row][col])
                    COLS[col].add(board[row][col])
                    ROWS[row].add(board[row][col])
        
        return True


