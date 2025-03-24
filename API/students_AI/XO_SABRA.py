# Constants
X = "X"
O = "O"
EMPTY = ""

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def score(board):
    winner = check_winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0

def successors(board, player):
    successors_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                successors_list.append(new_board)
    return successors_list

def get_move_priority(i, j):
    if (i, j) == (1, 1):
        return 3
    elif (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        return 2
    else: 
        return 1
    
def depth_limited_minimax(board, depth, is_maximizing):
        if check_winner(board) is not None:
            return score(board)
        if is_board_full(board):
            return 0
        if depth == 0:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for successor in successors(board, X):
                best_score = max(best_score, depth_limited_minimax(successor, depth - 1, False))
            return best_score
        else:
            best_score = float('inf')
            for successor in successors(board, O):
                best_score = min(best_score, depth_limited_minimax(successor, depth - 1, True))
            return best_score

def minimax1(board, player):
    depth_limit = 3
    best_move = None
    best_score = -float('inf') if player == X else float('inf')
    move_priority = -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                move_score = depth_limited_minimax(new_board, depth_limit, player == O)
                if (player == X and (move_score > best_score or (move_score == best_score and get_move_priority(i, j) > move_priority))) or \
                   (player == O and (move_score < best_score or (move_score == best_score and get_move_priority(i, j) > move_priority))):
                    best_score = move_score
                    best_move = (i, j)
                    move_priority = get_move_priority(i, j)

    return list(best_move) if best_move else [1, 1] 
def minimax2(board, player):
    def minimax_helper(board, is_maximizing):
        if check_winner(board) is not None:
            return score(board)
        if is_board_full(board):
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for successor in successors(board, X):
                best_score = max(best_score, minimax_helper(successor, False))
            return best_score
        else:
            best_score = float('inf')
            for successor in successors(board, O):
                best_score = min(best_score, minimax_helper(successor, True))
            return best_score

    best_move = None
    best_score = -float('inf') if player == X else float('inf')
    move_priority = -1 

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                move_score = minimax_helper(new_board, player == O)
                if (player == X and (move_score > best_score or (move_score == best_score and get_move_priority(i, j) > move_priority))) or \
                   (player == O and (move_score < best_score or (move_score == best_score and get_move_priority(i, j) > move_priority))):
                    best_score = move_score
                    best_move = (i, j)
                    move_priority = get_move_priority(i, j)

    return list(best_move) if best_move else [1, 1]