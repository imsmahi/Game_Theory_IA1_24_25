

X = "X"
O = "O"
EMPTY = ""
joueurMax = True



# Take board state as List of List contain 3 Rows and 3 Columns
# Example of initial state board :
# board = [     
#       [EMPTY, EMPTY, EMPTY],
#       [EMPTY, EMPTY, EMPTY],
#       [EMPTY, EMPTY, EMPTY]
# ]
#
# board can take 3 values (X,O,EMPTY)

import itertools

# X, O, EMPTY = "X", "O", None

def terminal(board):
    return winner(board) is not None or all(
        cell is not EMPTY for row in board for cell in row
    )

def winner(board):
    for player in (X, O):
        if (
            any(all(cell == player for cell in row) for row in board) or
            any(all(board[r][c] == player for r in range(3)) for c in range(3)) or
            all(board[i][i] == player for i in range(3)) or
            all(board[i][2 - i] == player for i in range(3))
        ):
            return player
    return None

def heuristic(board, player):
    opponent = X if player == O else O
    score = 0
    lines = list(board) + list(zip(*board))  
    lines.append([board[i][i] for i in range(3)])  
    lines.append([board[i][2 - i] for i in range(3)])  

    for line in lines:
        if line.count(player) == 2 and line.count(EMPTY) == 1:
            score += 10  
        if line.count(player) == 3:
            score += 100  
        if line.count(opponent) == 2 and line.count(EMPTY) == 1:
            score -= 10  
        if line.count(opponent) == 3:
            score -= 100  

    return score


def available_moves(board):
    moves = [
        (r, c) for r, c in itertools.product(range(3), repeat=2) if board[r][c] == EMPTY
    ]
    print(f"Coups possibles: {moves}")  # Vérifie si des coups sont disponibles
    return moves


def result(board, action, player):
    r, c = action
    if board[r][c] is not EMPTY:
        raise ValueError("Invalid move")

    new_board = tuple(
        tuple(cell if (i, j) != (r, c) else player for j, cell in enumerate(row))
        for i, row in enumerate(board)
    )

    return new_board

def minimax(board, depth, maximizing, player):
    if terminal(board) or depth == 0:
        return heuristic(board, player), None

    best_move = None
    if maximizing:
        best_value = float("-inf")
        for move in available_moves(board):
            new_board = result(board, move, player)
            value, _ = minimax(new_board, depth - 1, False, player)
            if value > best_value:
                best_value, best_move = value, move
    else:
        best_value = float("inf")
        opponent = X if player == O else O
        for move in available_moves(board):
            new_board = result(board, move, opponent)
            value, _ = minimax(new_board, depth - 1, True, player)
            if value < best_value:
                best_value, best_move = value, move

    return best_value, best_move

def is_one_move_played(board):
    return sum(cell in (X, O) for row in board for cell in row) == 1

def is_empty(board):
    return all(cell == EMPTY for row in board for cell in row)

def best_move(board, player):
    # maximizing = player ==   # X veut maximiser, O veut minimiser
    _, move = minimax(board, depth=3, maximizing=True, player=player)
    return move



def minimax1(board, player):
        print(best_move(board,player))
        # Return list contain 2 values (column, row)
        # Example:
        return best_move(board,player)




def minimax2(board, player):
        print(best_move(board,player))
        # Return list contain 2 values (column, row)
        # Example:
        return best_move(board,player)


board = [
    [X, O, O],
    [EMPTY, X, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

print(best_move(board, X))  # L'adversaire O doit jouer en minimisant
