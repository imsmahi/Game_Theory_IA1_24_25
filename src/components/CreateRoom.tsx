import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import { useGameStore } from '../store/gameStore';
import { createRoom, socket } from '../lib/socket';

const CreateRoom: React.FC = () => {

  
  const navigate = useNavigate();
  const { username, roomId, setUsername, setRoomId } = useGameStore();

  const handleCreateRoom = () => {
    if (!username) {
      alert('Please enter your username');
      return;
    }
    if (!roomId) {
      alert('Please enter a room ID');
      return;
    }

    // Emit the create_room event
    createRoom(roomId, username);

    // Listen for the room_created event
    socket.on('room_created', () => {
      navigate('/game'); // Navigate to the game page
    });

    // Listen for errors
    socket.on('room_token', () => {
      alert('This room is already token');
      return;
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 p-8">
      <div className="max-w-md mx-auto">
        <button
          onClick={() => navigate('/')}
          className="flex items-center text-white hover:text-blue-300 transition-colors mb-8"
        >
          <ArrowLeft className="w-6 h-6 mr-2" />
          Back to Dashboard
        </button>

        <div className="bg-white/10 backdrop-blur-sm rounded-xl p-8">
          <h2 className="text-2xl font-bold text-white mb-6">Create Room</h2>

          <div className="space-y-6">
            <div>
              <label className="block text-white text-sm font-medium mb-2">
                Your Username
              </label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter your username"
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div>
              <label className="block text-white text-sm font-medium mb-2">
                Room ID
              </label>
              <input
                type="text"
                value={roomId}
                onChange={(e) => setRoomId(e.target.value)}
                placeholder="Enter room ID"
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <button
              onClick={handleCreateRoom}
              className="w-full px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors"
            >
              Create Room
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateRoom;