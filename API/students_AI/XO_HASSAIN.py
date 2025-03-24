X = "X"
O = "O"
EMPTY = ""


def minimax(board, player):
    def gagne(board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(row[col] == player for row in board):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def rempli(board):
        return all(cell != EMPTY for row in board for cell in row)

    def evalue(board):
        if gagne(board, X):
            return 1
        if gagne(board, O):
            return -1
        return 0
    if gagne(board, X) or gagne(board, O) or rempli(board):
        score = evalue(board)
        return None 

    best_move = None

    if player == X:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = X
                    eval = evalue(board)
                    board[row][col] = EMPTY
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (row, col)

    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    eval = evalue(board)
                    board[row][col] = EMPTY
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (row, col)
    return best_move

board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

best_move = minimax(board, X)
