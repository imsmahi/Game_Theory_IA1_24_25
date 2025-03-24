import random

X = "X"
O = "O"
EMPTY = ""

# Combinaisons gagnantes
WINNING_COMBINATIONS = [
    [(0, 0), (0, 1), (0, 2)],  # Rows
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],  # Columns
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],  # Diagonals
    [(0, 2), (1, 1), (2, 0)]
]

def evaluate(board):
    """Retourne un score basé sur l'état du jeu."""
    for combination in WINNING_COMBINATIONS:
        values = [board[x][y] for x, y in combination]
        if values.count(X) == 3:
            return 10  # X gagne
        elif values.count(O) == 3:
            return -10  # O gagne

    return 0  # Match nul ou jeu non terminé

def get_available_moves(board):
    """Retourne toutes les cases vides sous forme de liste de tuples (x, y)."""
    return [(x, y) for x in range(3) for y in range(3) if board[x][y] == EMPTY]

def minimax(board, player, depth=3, maximizing=True):
    """Algorithme Minimax avec profondeur limitée."""
    score = evaluate(board)
    if score == 10 or score == -10 or depth == 0 or not get_available_moves(board):
        return score  # Retourne la valeur de l'état du jeu

    if maximizing:
        best_score = -float('inf')
        for x, y in get_available_moves(board):
            board[x][y] = X
            value = minimax(board, O, depth - 1, False)
            board[x][y] = EMPTY  # Annuler le coup
            best_score = max(best_score, value)
        return best_score
    else:
        best_score = float('inf')
        for x, y in get_available_moves(board):
            board[x][y] = O
            value = minimax(board, X, depth - 1, True)
            board[x][y] = EMPTY  # Annuler le coup
            best_score = min(best_score, value)
        return best_score

def best_move(board, player):
    """Trouve le meilleur coup pour un joueur donné."""
   # Si la cellule du centre est vide, la prendre immédiatement
    if board[1][1] == EMPTY:
        return (1, 1)

    best_score = -float('inf') if player == X else float('inf')
    move = None

    for x, y in get_available_moves(board):
        board[x][y] = player
        score = minimax(board, X if player == O else O, 3, player == X)
        board[x][y] = EMPTY  # Annuler le coup

        if (player == X and score > best_score) or (player == O and score < best_score):
            best_score = score
            move = (x, y)

    return move

def minimax_(board, player):
    best_move(board, player)
    moves = get_available_moves(board)
    return list(random.choice(moves)) if moves else [1, 1]
