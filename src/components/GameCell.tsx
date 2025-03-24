import React from 'react';
import { Circle, X } from 'lucide-react';
import { cn } from '../lib/utils';

interface GameCellProps {
  value: string | null;
  onClick: () => void;
  disabled: boolean;
}

const GameCell: React.FC<GameCellProps> = ({ value, onClick, disabled }) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={cn(
        "h-24 bg-white/5 backdrop-blur-sm rounded-lg",
        "flex items-center justify-center",
        "transition-all duration-200",
        "hover:bg-white/10 focus:outline-none focus:ring-2 focus:ring-blue-400",
        "disabled:cursor-not-allowed disabled:hover:bg-white/5"
      )}
    >
      {value === 'X' && <X className="w-12 h-12 text-blue-400" />}
      {value === 'O' && <Circle className="w-12 h-12 text-red-400" />}
    </button>
  );
};

export default GameCell;