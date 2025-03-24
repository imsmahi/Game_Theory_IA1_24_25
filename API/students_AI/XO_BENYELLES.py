X = "X"
O = "O"
EMPTY = ""

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return 1 if row[0] == X else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return 1 if board[0][col] == X else -1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return 1 if board[0][0] == X else -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return 1 if board[0][2] == X else -1
    return 0

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

def minimax1(board, player):
    score = evaluate(board)
    if score != 0 or not available_moves(board):
        return score
    
    if player == X:
        best_score = -float("inf")
        for r, c in available_moves(board):
            board[r][c] = X
            best_score = max(best_score, minimax1(board, O))
            board[r][c] = EMPTY
        return best_score
    else:
        best_score = float("inf")
        for r, c in available_moves(board):
            board[r][c] = O
            best_score = min(best_score, minimax1(board, X))
            board[r][c] = EMPTY
        return best_score

def best_move(board, player):
    best_score = -float("inf") if player == X else float("inf")
    move = None
    
    for r, c in available_moves(board):
        board[r][c] = player
        score = minimax1(board, player)
        board[r][c] = EMPTY
        
        if (player == X and score > best_score) or (player == O and score < best_score):
            best_score = score
            move = (r, c)
    
    return move
