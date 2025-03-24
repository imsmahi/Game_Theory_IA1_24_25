import math
import random

X = "X"
O = "O"
EMPTY = ""

def minimax1(board, player):
    return minimax(board, player, depth=3)

def minimax2(board, player):
    return minimax(board, player, depth=3)

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    return X if countO >= countX else O

def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def result(board, action):
    i, j = action
    board_copy = [row[:] for row in board]
    board_copy[i][j] = player(board)
    return board_copy

winning_patterns = [
    {(0,0), (0,1), (0,2)}, {(1,0), (1,1), (1,2)}, {(2,0), (2,1), (2,2)},
    {(0,0), (1,0), (2,0)}, {(0,1), (1,1), (2,1)}, {(0,2), (1,2), (2,2)},
    {(0,0), (1,1), (2,2)}, {(0,2), (1,1), (2,0)}
]

def checkwinner(board, p):
    player_positions = {(i,j) for i in range(3) for j in range(3) if board[i][j] == p}
    return any(pattern <= player_positions for pattern in winning_patterns)

def winner(board):
    if checkwinner(board, X): return X
    if checkwinner(board, O): return O
    return None

def terminal(board):
    return winner(board) is not None or not actions(board)

def utility(board):
    w = winner(board)
    if w == X: return 1
    if w == O: return -1
    return 0

cache = {}

def heuristic(board):
    x_score = 0
    o_score = 0
    for pattern in winning_patterns:
        x_count = o_count = empty = 0
        for (i,j) in pattern:
            if board[i][j] == X: x_count += 1
            elif board[i][j] == O: o_count += 1
            else: empty += 1
        
        if x_count == 2 and empty == 1: x_score += 1
        elif x_count == 1 and empty == 2: x_score += 0.2
        if o_count == 2 and empty == 1: o_score += 1
        elif o_count == 1 and empty == 2: o_score += 0.2
    return x_score - o_score

def minimax(board, p, depth=3, use_cache=True):
    if board == initial_state():
        return random.choice(actions(board))
    
    board_tuple = tuple(map(tuple, board))
    key = (board_tuple, depth)

    if use_cache and depth > 2 and key in cache:
        return cache[key]

    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        _, action = max_value(board, -math.inf, math.inf, depth)
    else:
        _, action = min_value(board, -math.inf, math.inf, depth)
    
    cache[key] = action
    return action

def max_value(board, alpha, beta, depth):
    if terminal(board):
        return utility(board), None
    if depth == 0:
        return heuristic(board), None

    v = -math.inf
    best_action = None
    for action in actions(board):
        new_depth = depth - 1
        min_val, _ = min_value(result(board, action), alpha, beta, new_depth)
        if min_val > v:
            v = min_val
            best_action = action
            if v == 1:
                break
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v, best_action

def min_value(board, alpha, beta, depth):
    if terminal(board):
        return utility(board), None
    if depth == 0:
        return heuristic(board), None

    v = math.inf
    best_action = None
    for action in actions(board):
        new_depth = depth - 1
        max_val, _ = max_value(result(board, action), alpha, beta, new_depth)
        if max_val < v:
            v = max_val
            best_action = action
            if v == -1:
                break
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v, best_action