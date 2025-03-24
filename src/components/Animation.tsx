export const Fireworks = () => (
    <div className="absolute inset-0 flex justify-center items-center pointer-events-none">
      <div className="relative w-full h-full">
        {[...Array(5)].map((_, i) => (
          <div
            key={i}
            className="absolute w-12 h-12 bg-purple-400 rounded-full opacity-75 animate-firework"
            style={{
              top: `${Math.random() * 80}%`,
              left: `${Math.random() * 80}%`,
              animationDelay: `${Math.random() * 1}s`
            }}
          />
        ))}
      </div>
    </div>
  );