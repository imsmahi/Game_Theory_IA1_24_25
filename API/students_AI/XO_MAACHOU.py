import time

X = "X"
O = "O"
EMPTY = ""

def check_winner(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_game_over(board):
    return check_winner(board, X) or check_winner(board, O) or all([cell != EMPTY for row in board for cell in row])

def evaluate(board):
    if check_winner(board, X):
        return 10  
    if check_winner(board, O):
        return -10 
    return 0  

error_count = 0  

def minimax1(board, player):
    global error_count
    start_time = time.time()

    if is_game_over(board):
        return evaluate(board), None, time.time() - start_time

    best_score = -float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = X
                score, _, _ = minimax2(board, O)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (col, row)
            else:
                if best_move is None:
                    error_count += 1  

    return best_score, best_move, time.time() - start_time

def minimax2(board, player):
    global error_count
    start_time = time.time()

    if is_game_over(board):
        return evaluate(board), None, time.time() - start_time

    best_score = float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = O
                score, _, _ = minimax1(board, X)
                board[row][col] = EMPTY

                if score < best_score:
                    best_score = score
                    best_move = (col, row)
            else:
                if best_move is None:
                    error_count += 1  

    return best_score, best_move, time.time() - start_time

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

_, first_move, execution_time = minimax1(board, X)

print("Premier coup recommandé:", first_move)
print("Temps d'exécution:", execution_time, "secondes")
print("Nombre d'erreurs:", error_count)
