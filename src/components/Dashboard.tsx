import React from 'react';
import { Users, User, BrainCircuit } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { useGameStore } from '../store/gameStore';
import { cn } from '../lib/utils';
//import { resetGame } from '../lib/socket';

const GameModeButton: React.FC<{
  icon: React.ReactNode;
  title: string;
  description: string;
  onClick: () => void;
  disabled?: boolean;
}> = ({ icon, title, description, onClick, disabled }) => (
  <button
    onClick={onClick}
    disabled={disabled}
    className={cn(
      "w-full p-8 bg-white/10 backdrop-blur-sm rounded-xl shadow-lg",
      "transition-all group",
      disabled
        ? "opacity-50 cursor-not-allowed"
        : "hover:bg-white/20"
    )}
  >
    <div className="flex flex-col items-center">
      <div className="mb-4 text-blue-400 group-hover:scale-110 transition-transform">
        {icon}
      </div>
      <h2 className="text-2xl font-semibold mb-2 text-white">{title}</h2>
      <p className="text-blue-200 text-center">{description}</p>
      {disabled && (
        <span className="mt-2 text-yellow-400 text-sm">Coming soon!</span>
      )}
    </div>
  </button>
);

const Dashboard: React.FC = () => {
  const navigate = useNavigate();
  const { setGameMode, resetGame } = useGameStore();

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-white mb-4">
            UABT AI Competition - Tic-Tac-Toe!
          </h1>
          <p className="text-lg text-blue-200">
            Attention, Master AI students! 🤖✨ It's time to put your skills to the test by developing your own artificial intelligence for the game of Tic-Tac-Toe.
          </p>
          <p className="text-lg text-blue-200">
            May the code be with you! 🚀🔥
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          <GameModeButton
            icon={<User className="w-12 h-12" />}
            title="Play Offline"
            description="Challenge a friend on the same device"
            onClick={() => {
              setGameMode('offline')
              resetGame()
              navigate('/game')
            }}
          />

          <GameModeButton
            icon={<Users className="w-12 h-12" />}
            title="Create Room"
            description="Start a new online game and invite friends"
            onClick={() => {
              resetGame()
              setGameMode('online')
              navigate('/create');
            }}
          />

          <GameModeButton
            icon={<Users className="w-12 h-12 text-green-400" />}
            title="Join Room"
            description="Join an existing game with a room code"
            onClick={() => {
              resetGame()
              setGameMode('online')

              navigate('/join')
            }}


          />

          <GameModeButton
            icon={<BrainCircuit className="w-12 h-12" />}
            title="Game Theory"
            description="A competition for Master's students in AI."
            onClick={() => {
              //setGameMode('AI')
              //resetGame()
              navigate('/game')
            }}
          />
        </div>
      </div>
      <footer className="mt-12 text-center text-blue-300 text-sm">
  &copy; {new Date().getFullYear()} University of Tlemcen - Department of Computer Science, Master AI. All rights reserved.
</footer>

    </div>

  );
};

export default Dashboard;