import React from 'react';
import { Trophy } from 'lucide-react';
import { useGameStore } from '../store/gameStore';
import { resetGame as resetFromServer } from '../lib/socket';

const GameStatus: React.FC = () => {
  const { currentPlayer, gameOver, winner, roomId, gameMode, resetGame } = useGameStore();

  const handleReset = () => {
    if (gameMode == 'offline' || gameMode == 'AI') {
      resetGame()
    }
    else {
      resetFromServer(roomId);
    }
    ;
  };

  return (
    <div className="space-y-4 mb-8 text-center">
      {!gameOver && (
        <div className="bg-white/10 backdrop-blur-sm rounded-lg p-6 text-white">
          <span className="text-2xl font-bold">
            Current Player: {currentPlayer}
          </span>
        </div>
      )}

      {gameOver && (
        <div className="bg-white/10 backdrop-blur-sm rounded-lg p-8 text-white">
          {winner ? (
            <div className="flex items-center justify-center space-x-3">
              <Trophy className="w-12 h-12 text-yellow-400" />
              <span className="text-3xl font-bold">
                {winner} Wins!
              </span>
            </div>
          ) : (
            <span className="text-3xl font-bold">It's a Draw!</span>
          )}

          <button
            onClick={handleReset}
            className="mt-6 px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors"
          >
            Play Again
          </button>
        </div>
      )}
    </div>
  );
};

export default GameStatus;