X = "X"
O = "O"
EMPTY = ""

def minimax1(board, player):
    """
    Minimax algorithm for Tic-Tac-Toe.
    Args:
        board: A 3x3 list representing the current state of the board.
        player: The current player ("X" or "O").
    Returns:
        A tuple ([row, col], score) representing the best move and its score.
    """
    # Base case: check if the game is over
    winner = check_winner(board)
    if winner is not None:
        if winner == "X":
            return None, 1  # X wins
        elif winner == "O":
            return None, -1  # O wins
        else:
            return None, 0  # Draw

    # Initialize best score and best move
    best_score = -float("inf") if player == "X" else float("inf")
    best_move = None

    # Iterate over all possible moves
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                # Make the move
                board[row][col] = player
                # Recursively evaluate the move
                move, score = minimax1(board, "O" if player == "X" else "X")
                # Undo the move
                board[row][col] = EMPTY

                # Update best move based on the player
                if player == "X":
                    if score > best_score:
                        best_score = score
                        best_move = [row, col]
                else:
                    if score < best_score:
                        best_score = score
                        best_move = [row, col]

    # Return the best move and its score
    return best_move, best_score
 

import random

def minimax2(board, player):
    """
    Random move generator for testing purposes.
    Args:
        board: A 3x3 list representing the current state of the board.
        player: The current player ("X" or "O").
    Returns:
        A list [row, col] representing a random valid move.
    """
    # Get all possible actions (valid moves)
    possible_actions = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.append([row, col])

    # If no valid moves are available, return None
    if not possible_actions:
        return None

    # Return a random valid move
    return random.choice(possible_actions)

def check_winner(board):
    """
    Helper function to check if there is a winner.
    Args:
        board: A 3x3 list representing the current state of the board.
    Returns:
        "X" if X wins, "O" if O wins, None if no winner.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None