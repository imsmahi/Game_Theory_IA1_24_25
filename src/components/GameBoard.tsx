import { useEffect, useState } from 'react';
import { useGameStore } from '../store/gameStore';
import playersData from '../data/players.json'; // Importation du JSON
import { PlayerPanel } from './PlayerPanel';
import { MatchPanel } from './MatchPanel';


const GameBoard = () => {
  const {
    board,
    gameOver,
    currentPlayer,
    winner,
    startAIBattle,
    player1Moves,
    player2Moves,
    battleInProgress,
    player1TotalTime,
    player1errorCount,
    player2TotalTime,
    player2errorCount,
  } = useGameStore();

  const [player1, setPlayer1] = useState(playersData[0].name);
  const [player2, setPlayer2] = useState(playersData[1].name);

  /* **************************************** */
  const [players, setPlayers] = useState(playersData);
  const [statsUpdated, setStatsUpdated] = useState(false);
  const [matchesUpdated, setMatchesUpdated] = useState(false);

  const updatePlayerStats = async () => {
    if (!gameOver || statsUpdated) return;

    const updatedPlayers = players.map((player) => {
      if (player.name === player1) {
        const updatedPlayer = {
          ...player,
          points: winner === "X"
            ? player.points + 3
            : winner === "O"
              ? player.points + 1
              : player.points + 2,
          wins: winner === 'X' ? player.wins + 1 : player.wins,
          losses: winner === 'O' ? player.losses + 1 : player.losses,
          draws: winner !== 'X' && winner !== 'O' ? player.draws + 1 : player.draws,
          totalTime: player.totalTime + player1TotalTime,
          totalErrors: player.totalErrors + player1errorCount,
        };
        //alert(`Player ${updatedPlayer.name} Wins: ${updatedPlayer.wins}`);
        return updatedPlayer;
      }
      if (player.name === player2) {
        const updatedPlayer = {
          ...player,
          points: winner === "O"
            ? player.points + 3
            : winner === "X"
              ? player.points + 1
              : player.points + 2,
          wins: winner === 'O' ? player.wins + 1 : player.wins,
          losses: winner === 'X' ? player.losses + 1 : player.losses,
          draws: winner !== 'X' && winner !== 'O' ? player.draws + 1 : player.draws,
          totalTime: player.totalTime + player2TotalTime,
          totalErrors: player.totalErrors + player2errorCount,
        };
        //alert(`Player ${updatedPlayer.name} Wins: ${updatedPlayer.wins}`);
        return updatedPlayer;
      }
      return player;
    });

    setPlayers(updatedPlayers);
    try {
      await fetch('http://localhost:5000/api/updatePlayers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedPlayers),
      });
      setStatsUpdated(true);
    } catch (error) {
      console.error('Erreur lors de la mise à jour des joueurs:', error);
    }
  };

  const updateMatchsStats = async () => {
    if (!gameOver || matchesUpdated) return; // ✅ Empêche l'exécution multiple

    //alert(matchesUpdated)
    const match = {
      startTime: new Date().toISOString(),
      opponent1: player1,
      opponent1Point: winner === "X"
        ? 3
        : winner === "O"
          ? 1
          : 2,
      opponent1totalTime: player1TotalTime,
      opponent1errorCount: player1errorCount,
      opponent2: player2,
      opponent2Point: winner === "O"
        ? 3
        : winner === "X"
          ? 1
          : 2,
      opponent2totalTime: player2TotalTime,
      opponent2errorCount: player2errorCount,
    };

    try {
      await fetch('http://localhost:5000/api/updateMatches', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(match), // ✅ Envoi du bon objet
      });

      setMatchesUpdated(true); // ✅ Mise à jour de l'état après succès
    } catch (error) {
      console.error('Erreur lors de la mise à jour des matches:', error);
    }
  };

  /** */

  useEffect(() => {
    if (gameOver && !statsUpdated && !matchesUpdated) {
      updatePlayerStats();
      updateMatchsStats();
    }

  }, [gameOver, statsUpdated, matchesUpdated]);

  /* **************************************** */
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 flex justify-center items-start py-8">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-[230px_1fr_230px] gap-4 justify-items-center items-start p-0">

          {/* Player 1 Panel */}
          <PlayerPanel
            player="X"
            winner={winner}
            currentPlayer={currentPlayer}
            totalTime={player1TotalTime}
            errorCount={player1errorCount}
            moves={player1Moves}
            color="blue"
            selectedPlayer={player1}
            setSelectedPlayer={setPlayer1}
          />

          {/* Game Board */}
          <div className="flex flex-col items-center justify-center flex-1">
            <div className="text-center mb-8">
              <h1 className="text-4xl font-bold text-white mb-4">AI Battle Mode</h1>
              {gameOver ? (
                <p className="text-2xl text-blue-200">
                  {winner ? `${winner} Wins! 🎉` : "It's a Draw!"}
                </p>
              ) : (
                <p className="text-xl text-blue-200">
                  {battleInProgress ? `Current Player: ${currentPlayer}` : 'Ready to Battle'}
                </p>
              )}
            </div>

            <div className="grid grid-cols-3 gap-4 mb-8">
              {board.map((row, i) =>
                row.map((cell, j) => (
                  <div
                    key={`${i}-${j}`}
                    className={`h-24 w-24 bg-white/5 backdrop-blur-sm rounded-lg
                      flex items-center justify-center text-4xl font-bold
                      ${cell === 'X' ? 'text-blue-400' : 'text-red-400'}`}
                  >
                    {cell}
                  </div>
                ))
              )}
            </div>

            <button
              onClick={() => {
                setStatsUpdated(false); // Réinitialisation de statsUpdated avant de commencer
                setMatchesUpdated(false); // Réinitialisation de matchesUpdated avant de commencer
                startAIBattle(player1, player2); // Lancer la bataille AI
              }}
              disabled={battleInProgress}
              className="px-8 py-4 bg-blue-500 hover:bg-blue-600 disabled:bg-blue-800
                text-white font-bold rounded-lg shadow-lg transition-colors
                disabled:cursor-not-allowed"
            >
              {battleInProgress ? 'Battle in Progress...' : 'Start AI Battle'}
            </button>
          </div>

          {/* Player 2 Panel */}
          <PlayerPanel
            player="O"
            winner={winner}
            currentPlayer={currentPlayer}
            totalTime={player2TotalTime}
            errorCount={player2errorCount}
            moves={player2Moves}
            color="red"
            selectedPlayer={player2}
            setSelectedPlayer={setPlayer2}
          />
        </div>
        {/* Match Panel */}
        <MatchPanel players={players} />

        {/* Copyright Footer */}
        <footer className="mt-12 text-center text-blue-300 text-sm py-4">
          &copy; {new Date().getFullYear()} University of Tlemcen - Department of Computer Science, Master AI. All rights reserved.
        </footer>
      </div>
    </div>
  );
};

export default GameBoard;
