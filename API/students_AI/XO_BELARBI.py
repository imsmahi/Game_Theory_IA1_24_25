import math
import random

X = "X"
O = "O"
EMPTY = ""

#Debut

# Profondeur maximale dynamique
MAX_DEPTH = 5  
transposition_table = {}  # Table de transposition pour mémoïsation


def check_winner0(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False


def winner0(board):
    if check_winner0(board, X):
        return X
    elif check_winner0(board, O):
        return O
    return None


def terminal0(board):
    return winner0(board) is not None or all(board[i][j] != EMPTY for i in range(3) for j in range(3))


def heuristic0(board):
    score = 0
    
    if board[1][1] == X:
        score += 50
    elif board[1][1] == O:
        score -= 50

    for (i, j) in [(0,0), (0,2), (2,0), (2,2)]:
        if board[i][j] == X:
            score += 30
        elif board[i][j] == O:
            score -= 30

    for (i, j) in [(0,1), (1,0), (1,2), (2,1)]:
        if board[i][j] == X:
            score += 10
        elif board[i][j] == O:
            score -= 10
    
    # Évaluation des lignes, colonnes et diagonales
    for i in range(3):
        row = [board[i][j] for j in range(3)]
        col = [board[j][i] for j in range(3)]
        score += evaluate_line0(row, X, O)
        score += evaluate_line0(col, X, O)
    
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    score += evaluate_line0(diag1, X, O)
    score += evaluate_line0(diag2, X, O)
    
    return score


def evaluate_line0(line, player, opponent):
    if line.count(player) == 2 and line.count(EMPTY) == 1:
        return 100
    elif line.count(player) == 1 and line.count(EMPTY) == 2:
        return 10
    elif line.count(opponent) == 2 and line.count(EMPTY) == 1:
        return -100
    elif line.count(opponent) == 1 and line.count(EMPTY) == 2:
        return -10
    return 0


def board_to_tuple0(board):
    return tuple(tuple(row) for row in board)


def dynamic_depth0(board):
    empty_count = sum(row.count(EMPTY) for row in board)
    return 7 if empty_count > 6 else 5 if empty_count > 3 else 3


def minimax0(board, depth, is_maximizing):
    board_key = board_to_tuple0(board)
    if board_key in transposition_table:
        return transposition_table[board_key]
    
    max_depth = dynamic_depth0(board)
    if terminal0(board) or depth >= max_depth:
        if winner0(board) == X:
            return 1000 - depth, None  
        elif winner0(board) == O:
            return depth - 1000, None  
        else:
            return heuristic0(board), None

    best_action = None
    moves = [(1, 1)] + [(i, j) for i in [0, 2] for j in [0, 2]] + [(i, j) for i in [0, 1, 2] for j in [0, 1, 2] if (i, j) not in [(1,1),(0,0),(0,2),(2,0),(2,2)]]
    
    if is_maximizing:
        max_eval = -math.inf
        for i, j in moves:
            if board[i][j] == EMPTY:
                board[i][j] = X
                eval, _ = minimax0(board, depth + 1, False)
                board[i][j] = EMPTY  
                if eval > max_eval:
                    max_eval = eval
                    best_action = (i, j)
        transposition_table[board_key] = (max_eval, best_action)
        return max_eval, best_action
    else:
        min_eval = math.inf
        for i, j in moves:
            if board[i][j] == EMPTY:
                board[i][j] = O
                eval, _ = minimax0(board, depth + 1, True)
                board[i][j] = EMPTY  
                if eval < min_eval:
                    min_eval = eval
                    best_action = (i, j)
        transposition_table[board_key] = (min_eval, best_action)
        return min_eval, best_action


def minimax1(board, player):
    if all(board[i][j] == EMPTY for i in range(3) for j in range(3)):
        return [1, 1]  
    _, best_move = minimax0(board, 0, player == X)
    return list(best_move) if best_move else random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY])

#fin



def minimax2(board, player):

    if all(board[i][j] == EMPTY for i in range(3) for j in range(3)):
        return [1, 1]  
    _, best_move = minimax0(board, 0, player == O)
    return list(best_move) if best_move else random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY])
