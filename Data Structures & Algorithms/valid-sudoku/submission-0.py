class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_row = set()
            seen_col = set()
            seen_square = set()
            for j in range(9):
                # Check rows
                if board[i][j] != ".":
                    if board[i][j] in seen_row:
                        return False
                    seen_row.add(board[i][j])
                
                # Check columns
                if board[j][i] != ".":
                    if board[j][i] in seen_col:
                        return False
                    seen_col.add(board[j][i])
                
                # Check 3x3 squares
                row_idx = 3 * (i // 3) + j // 3
                col_idx = 3 * (i % 3) + j % 3
                if board[row_idx][col_idx] != ".":
                    if board[row_idx][col_idx] in seen_square:
                        return False
                    seen_square.add(board[row_idx][col_idx])

        return True