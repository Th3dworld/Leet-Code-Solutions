class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        grid = collections.defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in row[r]:
                    return False
                elif board[r][c] in col[c]:
                    return False
                elif board[r][c] in grid[(r//3,c//3)]:
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    grid[(r//3,c//3)].add(board[r][c])
        return True