class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        grid = collections.defaultdict(set)
        
        for ROW in range(len(board)):
            for COL in range(len(board)):
                if board[ROW][COL] == ".":
                    continue
                    
                if board[ROW][COL] in row[ROW]:
                    return False
                else:
                    row[ROW].add(board[ROW][COL])
                
                if board[ROW][COL] in col[COL]:
                    return False
                else:
                    col[COL].add(board[ROW][COL])
                
                if board[ROW][COL] in grid[(ROW//3, COL//3)]:
                    return False
                else:
                    grid[(ROW//3, COL//3)].add(board[ROW][COL])
                
        return True
                    
                  
