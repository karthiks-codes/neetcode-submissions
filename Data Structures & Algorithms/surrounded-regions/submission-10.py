class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        def temp(r, c):
            if r < 0 or r == row or c < 0 or c == col or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            temp(r + 1, c)
            temp(r - 1, c)
            temp(r, c + 1)
            temp(r, c - 1)

        for r in range(row):
            temp(r, 0)
            temp(r, col - 1)
            
        for c in range(col):
            temp(0, c)
            temp(row - 1, c)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        

    
            