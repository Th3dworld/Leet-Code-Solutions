class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = collections.defaultdict(set)
        COLS = collections.defaultdict(set)
        GRID = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in ROWS[row] or board[row][col] in COLS[col] or board[row][col] in GRID[(row//3,col//3)]:
                    return False
                else:
                    ROWS[row].add(board[row][col])
                    COLS[col].add(board[row][col])
                    GRID[(row//3,col//3)].add(board[row][col])
        return True
