X = "X"
O = "O"
EMPTY = ""

def minimax1(board, player):
    def check_winner(b):
        for row in b:
            if row[0] == row[1] == row[2] and row[0] != EMPTY:
                return row[0]
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col] and b[0][col] != EMPTY:
                return b[0][col]
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] != EMPTY:
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] != EMPTY:
            return b[0][2]
        return None

    def is_board_full(b):
        for row in b:
            if EMPTY in row:
                return False
        return True

    def make_move(b, row, col, p):
        new_board = [r.copy() for r in b]
        new_board[row][col] = p
        return new_board

    def get_possible_moves(b):
        moves = []
        if b[1][1] == EMPTY:
            moves.append((1, 1))
        for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if b[row][col] == EMPTY:
                moves.append((row, col))
        for row, col in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if b[row][col] == EMPTY:
                moves.append((row, col))
        return moves

    def minimax_value(b, p, depth):
        winner = check_winner(b)
        if winner is not None:
            return 10 - depth if winner == X else depth - 10
        if is_board_full(b):
            return 0

        moves = get_possible_moves(b)
        if p == X:
            max_score = -float('inf')
            for r, c in moves:
                new_b = make_move(b, r, c, X)
                score = minimax_value(new_b, O, depth + 1)
                if score > max_score:
                    max_score = score
            return max_score
        else:
            min_score = float('inf')
            for r, c in moves:
                new_b = make_move(b, r, c, O)
                score = minimax_value(new_b, X, depth + 1)
                if score < min_score:
                    min_score = score
            return min_score

    best_score = -float('inf') if player == X else float('inf')
    best_move = None
    for row, col in get_possible_moves(board):
        new_board = make_move(board, row, col, player)
        next_player = O if player == X else X
        current_score = minimax_value(new_board, next_player, 1)
        if (player == X and current_score > best_score) or (player == O and current_score < best_score):
            best_score = current_score
            best_move = [col, row]
    return best_move if best_move is not None else [1, 1]

def minimax2(board, player):
    def check_winner(b):
        for row in b:
            if row[0] == row[1] == row[2] and row[0] != EMPTY:
                return row[0]
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col] and b[0][col] != EMPTY:
                return b[0][col]
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] != EMPTY:
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] != EMPTY:
            return b[0][2]
        return None

    def is_board_full(b):
        for row in b:
            if EMPTY in row:
                return False
        return True

    def make_move(b, row, col, p):
        new_board = [r.copy() for r in b]
        new_board[row][col] = p
        return new_board

    def get_possible_moves(b):
        moves = []
        if b[1][1] == EMPTY:
            moves.append((1, 1))
        for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if b[row][col] == EMPTY:
                moves.append((row, col))
        for row, col in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if b[row][col] == EMPTY:
                moves.append((row, col))
        return moves

    def minimax_value(b, p, depth):
        winner = check_winner(b)
        if winner is not None:
            return 10 - depth if winner == X else depth - 10
        if is_board_full(b):
            return 0

        moves = get_possible_moves(b)
        if p == X:
            max_score = -float('inf')
            for r, c in moves:
                new_b = make_move(b, r, c, X)
                score = minimax_value(new_b, O, depth + 1)
                max_score = max(max_score, score)
            return max_score
        else:
            min_score = float('inf')
            for r, c in moves:
                new_b = make_move(b, r, c, O)
                score = minimax_value(new_b, X, depth + 1)
                min_score = min(min_score, score)
            return min_score

    best_score = -float('inf') if player == X else float('inf')
    best_move = None
    for row, col in get_possible_moves(board):
        new_board = make_move(board, row, col, player)
        next_player = O if player == X else X
        current_score = minimax_value(new_board, next_player, 1)
        if (player == X and current_score > best_score) or (player == O and current_score < best_score):
            best_score = current_score
            best_move = [col, row]
    return best_move if best_move is not None else [1, 1]