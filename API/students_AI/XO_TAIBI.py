X = "X"
O = "O"
EMPTY = ""


class Node:
    WIN_LINES = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def __init__(self):
        self.evaluation = None
        self.move = []
        self.nextMove = []
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.children = []

    def add_child(self, child: "Node") -> "Node":
        self.children.append(child)
        return self

    def copy_board(self, board: list[list[str]]):
        self.board = [row[:] for row in board]

    def has_full_board(self) -> bool:
        for row in self.board:
            if "" in row:
                return False
        return True

    def has_final_game_board(self) -> bool:
        for line in self.WIN_LINES:
            cells = [self.board[i][j] for i, j in line]
            if cells[0] != "" and cells.count(cells[0]) == 3:
                return True
        return False

    def is_leaf(self) -> bool:
        return self.has_full_board() or self.has_final_game_board()

    def is_depth_limit(self) -> bool:
        return len(self.children) == 0


def evaluate(N: Node, is_x_player: bool) -> None:
    player_marker = "X" if is_x_player else "O"
    opponent_marker = "O" if is_x_player else "X"

    winning = losing = winningInNextMove = losingInNextMove = possibleWins = (
        possibleLoses
    ) = 0

    rows = [{"player": 0, "opponent": 0, "empty": 0} for _ in range(3)]
    cols = [{"player": 0, "opponent": 0, "empty": 0} for _ in range(3)]
    diag = {"player": 0, "opponent": 0, "empty": 0}
    anti_diag = {"player": 0, "opponent": 0, "empty": 0}

    for i in range(3):
        for j in range(3):
            cell = N.board[i][j]
            if cell == player_marker:
                rows[i]["player"] += 1
                cols[j]["player"] += 1
                if i == j:
                    diag["player"] += 1
                if i + j == 2:
                    anti_diag["player"] += 1
            elif cell == opponent_marker:
                rows[i]["opponent"] += 1
                cols[j]["opponent"] += 1
                if i == j:
                    diag["opponent"] += 1
                if i + j == 2:
                    anti_diag["opponent"] += 1
            else:
                rows[i]["empty"] += 1
                cols[j]["empty"] += 1
                if i == j:
                    diag["empty"] += 1
                if i + j == 2:
                    anti_diag["empty"] += 1

    lines = rows + cols + [diag, anti_diag]

    for counts in lines:
        if counts["player"] == 3:
            winning += 1
        elif counts["opponent"] == 3:
            losing += 1

        if counts["player"] == 2 and counts["empty"] == 1:
            winningInNextMove += 1
        elif counts["opponent"] == 2 and counts["empty"] == 1:
            losingInNextMove += 1

        if counts["player"] == 1 and counts["empty"] == 2:
            possibleWins += 1
        elif counts["opponent"] == 1 and counts["empty"] == 2:
            possibleLoses += 1

    N.evaluation = (
        1000 * (winning - losing)
        + 100 * (winningInNextMove - losingInNextMove)
        + 10 * (possibleWins - possibleLoses)
    )


memory = None


def generate_depth(
    N: Node, is_x_player: bool, depth: int, next_x_player: bool, memory=None
) -> None:
    if memory is None:
        memory = {}

    board_key = tuple(tuple(row) for row in N.board)
    if board_key in memory:
        N.evaluation = memory[board_key]
        return

    if depth == 0 or N.is_leaf():
        evaluate(N, is_x_player)
        memory[board_key] = N.evaluation
        return

    available_moves = [
        (i, j) for i in range(3) for j in range(3) if N.board[i][j] == ""
    ]

    for i, j in available_moves:
        child = Node()
        child.copy_board(N.board)
        child.move = [i, j]
        child.board[i][j] = "X" if next_x_player else "O"
        N.add_child(child)
        generate_depth(child, is_x_player, depth - 1, not next_x_player, memory)


def minimax(N: Node, maxPlayer: bool = True) -> int:
    if N.is_depth_limit():
        return N.evaluation
    if maxPlayer:
        v = float("-inf")
        for i in N.children:
            temp = minimax(i, not maxPlayer)
            if temp > v:
                v = temp
                N.nextMove = i.move
    else:
        v = float("inf")
        for i in N.children:
            temp = minimax(i, not maxPlayer)
            if temp < v:
                v = temp
                N.nextMove = i.move
    return v


def fixBoard(board: list[list[str]]) -> list[list[str]]:
    return [[cell if cell != None else "" for cell in row] for row in board]


def bestMove(board: list[list[str]], is_x_player: str):
    N = Node()
    N.copy_board(fixBoard(board))
    global memory
    generate_depth(N, is_x_player == "X", 3, is_x_player == "X", memory)
    minimax(N)
    return N.nextMove


def minimax1(board, player):
    return bestMove(board, player)


def minimax2(board, player):
    return bestMove(board, player)
