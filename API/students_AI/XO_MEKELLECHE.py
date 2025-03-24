X = "X"
O = "O"
EMPTY = ""

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    return winner(board) is not None or all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def utility(board):
    win = winner(board)
    return 1 if win == X else -1 if win == O else 0

def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def result(board, action, player):
    i, j = action
    new_board = [row[:] for row in board]
    new_board[i][j] = player
    return new_board

def minimax(board, player, alpha=-float('inf'), beta=float('inf')):
    if terminal(board):
        return None, utility(board)
    
    best_move = None

    if player == X:
        max_value = -float('inf')
        for action in actions(board):
            new_board = result(board, action, player)
            _, value = minimax(new_board, O, alpha, beta)
            if value > max_value:
                max_value = value
                best_move = action
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, max_value

    else:
        min_value = float('inf')
        for action in actions(board):
            new_board = result(board, action, player)
            _, value = minimax(new_board, X, alpha, beta)
            if value < min_value:
                min_value = value
                best_move = action
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, min_value


def minimax1(board, player):
    best_move, _ = minimax(board, player)
    return list(best_move) if best_move else [1, 1]

def minimax2(board, player):
    best_move, _ = minimax(board, player)
    return list(best_move) if best_move else [1, 1]
