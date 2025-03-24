export type Player = 'X' | 'O';
export type Cell = Player | null;
export type GameMode = 'offline' | 'online';
export type GameStatus = 'playing' | 'won' | 'draw';
export type RoomStatus = 'creating' | 'joining' | null;

export interface GameState {
  board: Cell[];
  currentPlayer: Player;
  gameMode: GameMode;
  gameStatus: GameStatus;
  winner: Player | null;
  gameId: string | null;
  roomStatus: RoomStatus;
  scores: {
    X: number;
    O: number;
  };
}