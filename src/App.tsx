import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useGameStore } from './store/gameStore';
import { socket } from './lib/socket';
import Dashboard from './components/Dashboard';
import CreateRoom from './components/CreateRoom';
import JoinRoom from './components/JoinRoom';
import GameBoard from './components/GameBoard';
import GameStatus from './components/GameStatus';

const Game: React.FC = () => {
  const { updateGame, resetGame } = useGameStore();

  useEffect(() => {

    const handleRoomJoined = (data: { message: string }) => {
      console.log('Room joined:', data);

    };

    const handleUpdateGame = (data: {
      board: [['', '', ''], ['', '', ''], ['', '', '']];
      current_player: string;
      terminal?: boolean;
      winner?: string;
    }) => {
      console.log('Game updated:', data);
      updateGame(data);
    };


    const handleGameStarted = (data: { message: string }) => {
      console.log("game start message");
      alert(data.message);
    };

    const handleResetGame = (data: { message: string; first_player: string }) => {
      console.log("reset game");
      alert(data.message);
      resetGame();
    };

    const handleError = (data: { message: string }) => {
      alert("Error unaccepted: " + data.message);
    };


    socket.on('room_joined', handleRoomJoined);
    socket.on('update_game', handleUpdateGame);
    socket.on('game_started', handleGameStarted);
    socket.on('reset_game', handleResetGame);
    socket.on('error', handleError);

    return () => {
      socket.off('room_created', handleRoomJoined);
      socket.off('room_joined', handleRoomJoined);
      socket.off('update_game', handleUpdateGame);
      socket.off('game_started', handleGameStarted);
      socket.off('reset_game', handleResetGame);
      socket.off('error', handleError);
    };
  }, [updateGame, resetGame]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-white mb-4">
            Who will create the unbeatable AI? 🏆
          </h1>
          <p className="text-lg text-blue-200">
            Only the smartest AI will triumph! 🏆
          </p>
        </div>

        <GameStatus />
        <GameBoard />
      </div>
    </div>
  );
};

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/create" element={<CreateRoom />} />
        <Route path="/join" element={<JoinRoom />} />
        <Route path="/game" element={<Game />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;