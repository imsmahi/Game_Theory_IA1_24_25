import React from 'react';
import { Home, RotateCcw } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useGameStore } from '../store/gameStore';

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const { resetGame } = useGameStore();

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900">
      <div className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <Link 
            to="/" 
            className="flex items-center text-white hover:text-blue-300 transition-colors"
          >
            <Home className="w-6 h-6 mr-2" />
            <span className="font-semibold">Home</span>
          </Link>
          <button
            onClick={resetGame}
            className="flex items-center text-white hover:text-blue-300 transition-colors"
          >
            <RotateCcw className="w-6 h-6 mr-2" />
            <span className="font-semibold">Reset Game</span>
          </button>
        </div>
        {children}
      </div>
    </div>
  );
};

export default Layout;