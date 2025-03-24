import { Board } from '../types/game';

// Check for a winner
export const checkWinner = (board: Board): string | null => {
  // Check rows
  for (let i = 0; i < 3; i++) {
    if (board[i][0] && board[i][0] === board[i][1] && board[i][0] === board[i][2]) {
      return board[i][0];
    }
  }

  // Check columns
  for (let j = 0; j < 3; j++) {
    if (board[0][j] && board[0][j] === board[1][j] && board[0][j] === board[2][j]) {
      return board[0][j];
    }
  }

  // Check diagonals
  if (board[0][0] && board[0][0] === board[1][1] && board[0][0] === board[2][2]) {
    return board[0][0];
  }
  if (board[0][2] && board[0][2] === board[1][1] && board[0][2] === board[2][0]) {
    return board[0][2];
  }

  return null;
};

// Check if the game is a draw
export const isDraw = (board: Board): boolean => {
  return board.every(row => row.every(cell => cell !== ''));
};

// Check if the game is over (either won or drawn)
export const isGameOver = (board: Board): boolean => {
  return !!checkWinner(board) || isDraw(board);
};