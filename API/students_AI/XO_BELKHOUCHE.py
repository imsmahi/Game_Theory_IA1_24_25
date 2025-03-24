X = "X"
O = "O"
EMPTY = ""

def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def check_terminal(board):
    # Check if X won
    if check_winner(board, X):
        return True, X
    
    # Check if O won
    if check_winner(board, O):
        return True, O
    
    # Check for draw (board is full)
    is_full = all(cell != EMPTY for row in board for cell in row)
    if is_full:
        return True, None  # Draw
    
    return False, None  # Game still in progress

def evaluate_board(board):
    # Check if X won
    if check_winner(board, X):
        return 10
    
    # Check if O won
    if check_winner(board, O):
        return -10
    
    # Draw
    return 0

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, is_maximizing, player):
    opponent = O if player == X else X
    score = evaluate_board(board)
    
    # If Maximizer or Minimizer has won the game, return score
    if score == 10 or score == -10:
        return score
    
    # If there are no more moves and no winner, it's a draw
    if not get_available_moves(board):
        return 0
    
    # Maximizer's move
    if is_maximizing:
        best_score = -1000
        for i, j in get_available_moves(board):
            board[i][j] = player
            best_score = max(best_score, minimax(board, depth + 1, False, player))
            board[i][j] = EMPTY  # Undo move
        return best_score
    
    # Minimizer's move
    else:
        best_score = 1000
        for i, j in get_available_moves(board):
            board[i][j] = opponent
            best_score = min(best_score, minimax(board, depth + 1, True, player))
            board[i][j] = EMPTY  # Undo move
        return best_score

def get_best_move(board, player):
    opponent = O if player == X else X
    board_copy = [row[:] for row in board]
    
    best_score = -1000 if player == X else 1000
    best_move = None
    
    for i, j in get_available_moves(board_copy):
        board_copy[i][j] = player
        score = minimax(board_copy, 0, player == O, player)
        board_copy[i][j] = EMPTY  # Undo the move
        
        if (player == X and score > best_score) or (player == O and score < best_score):
            best_score = score
            best_move = (i, j)
    
    return list(best_move) if best_move else None
