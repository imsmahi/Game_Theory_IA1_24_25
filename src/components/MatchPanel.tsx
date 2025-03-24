import { useState } from 'react';
import matchesData from '../data/matches.json'; // ✅ Importation des matchs
import playersData from '../data/players.json'; // ✅ Importation des joueurs

interface Player {
    name: string;
    points: number;
    wins: number;
    losses: number;
    draws: number;
    totalTime: number;
    totalErrors: number;
}

interface MatchPanelProps {
    players: Player[];
}

export const MatchPanel = ({ players }: MatchPanelProps) => {
    const [activeTab, setActiveTab] = useState("matches");

    // Liste des journées disponibles
    const matchDays = Array.from(new Set(matchesData.map(match => match.matchDay))).sort((a, b) => a - b);
    const [selectedDay, setSelectedDay] = useState(matchDays[0]);

    const [selectedPlayer, setSelectedPlayer] = useState(players[0]?.name || "");

    // Filtrer les matchs de la journée sélectionnée
    const matchesOfTheDay = matchesData.filter(match => match.matchDay === selectedDay);

    // Filtrer les matchs du joueur sélectionné
    const playerMatches = matchesData.filter(match => match.opponent1 === selectedPlayer || match.opponent2 === selectedPlayer).
    sort((a, b) => new Date(a.startTime).getTime() - new Date(b.startTime).getTime());

    // Calcul du classement avec tri avancé
    const ranking = [...players]
        .map(player => {
            const playerData = playersData.find(p => p.name === player.name) || {
                points: 0,
                wins: 0,
                losses: 0,
                draws: 0,
                totalTime: 0,
                totalErrors: 0,
            };
            return {
                name: player.name,
                points: playerData.points,
                wins: playerData.wins,
                losses: playerData.losses,
                draws: playerData.draws,
                totalMatches: playerData.wins + playerData.losses + playerData.draws,
                totalTime: playerData.totalTime,
                totalErrors: playerData.totalErrors,
            };
        })
        .sort((a, b) =>
            b.points - a.points ||
            a.totalTime - b.totalTime ||
            a.totalErrors - b.totalErrors
        );

    return (
        <div className="mt-8 bg-gray-800 p-6 rounded-lg shadow-lg">
            {/* Tabs */}
            <div className="flex border-b border-gray-600 mb-4">
                <button
                    className={`p-2 flex-1 text-center ${activeTab === "matches" ? "border-b-2 border-blue-400 text-blue-400" : "text-gray-300"}`}
                    onClick={() => setActiveTab("matches")}
                >
                    Liste des Matchs
                </button>
                <button
                    className={`p-2 flex-1 text-center ${activeTab === "ranking" ? "border-b-2 border-blue-400 text-blue-400" : "text-gray-300"}`}
                    onClick={() => setActiveTab("ranking")}
                >
                    Classement
                </button>
                <button
                    className={`p-2 flex-1 text-center ${activeTab === "player" ? "border-b-2 border-blue-400 text-blue-400" : "text-gray-300"}`}
                    onClick={() => setActiveTab("player")}>
                    Joueur
                </button>
            </div>

            {/* Onglet des matchs avec Sélecteur de journées */}
            {activeTab === "matches" && (
                <>
                    <div className="mb-4">
                        <label className="text-white text-sm">Sélectionner une journée :</label>
                        <select
                            className="w-full bg-gray-800 text-white text-lg rounded-lg p-2 border border-gray-600 mt-2"
                            value={selectedDay}
                            onChange={(e) => setSelectedDay(Number(e.target.value))}
                        >
                            {matchDays.map(day => (
                                <option key={day} value={day}>Journée {day}</option>
                            ))}
                        </select>
                    </div>

                    <table className="w-full bg-white text-black rounded-lg overflow-hidden shadow-lg">
                        <thead className="bg-gray-200">
                            <tr>
                                <th className="p-2">Date & Heure</th>
                                <th className="p-2">Joueur 1</th>
                                <th className="p-2">Score</th>
                                <th className="p-2">Joueur 2</th>
                            </tr>
                        </thead>
                        <tbody>
                            {matchesOfTheDay.map((match, index) => {
                                const date = new Date(match.startTime);
                                const formattedDate = `${date.toLocaleDateString()} ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;

                                return (
                                    <tr key={index} className="text-center border-b">
                                        <td className="p-2">{formattedDate}</td>
                                        <td className="p-2">{match.opponent1}</td>
                                        <td className="p-2 font-bold">
                                            <table className="w-full border-collapse border border-gray-300 text-xs">
                                                <thead>
                                                    <tr className="border border-gray-300 bg-gray-200">
                                                        <td className="p-1 text-lg text-center" colSpan={3}>
                                                            {match.opponent1Point} - {match.opponent2Point}
                                                        </td>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr className="border border-gray-300">
                                                        <td className="p-1 font-bold text-left">⏱ Temps (sec)</td>
                                                        <td className="p-1 text-center">{match.opponent1totalTime}</td>
                                                        <td className="p-1 text-center">{match.opponent2totalTime}</td>
                                                    </tr>
                                                    <tr className="border border-gray-300">
                                                        <td className="p-1 font-bold text-left">⛔ Erreurs</td>
                                                        <td className="p-1 text-center">{match.opponent1errorCount}</td>
                                                        <td className="p-1 text-center">{match.opponent2errorCount}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                        <td className="p-2">{match.opponent2}</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </>
            )}

            {/* Onglet Classement */}
            {activeTab === "ranking" && (
                <table className="w-full bg-white text-black rounded-lg overflow-hidden shadow-lg">
                    <thead className="bg-gray-200">
                        <tr>
                            <th className="p-2">Position</th>
                            <th className="p-2">Joueur</th>
                            <th className="p-2">Points</th>
                            <th className="p-2">Joués</th>
                            <th className="p-2">Gagnés</th>
                            <th className="p-2">Perdus</th>
                            <th className="p-2">Nuls</th>
                            <th className="p-2">Time</th>
                            <th className="p-2">Errors</th>
                        </tr>
                    </thead>
                    <tbody>
                        {ranking.map((player, index) => (
                            <tr key={index} className="text-center border-b">
                                <td className="p-2">{index + 1}</td>
                                <td className="p-2 text-left">{player.name}</td>
                                <td className="p-2 font-bold">{player.points}</td>
                                <td className="p-2">{player.totalMatches}</td>
                                <td className="p-2">{player.wins}</td>
                                <td className="p-2">{player.losses}</td>
                                <td className="p-2">{player.draws}</td>
                                <td className="p-2">{player.totalTime} sec</td>
                                <td className="p-2">{player.totalErrors}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}

            {/* Onglet liste des matches par joueur*/}
            {activeTab === "player" && (
                <>
                    <label className="text-white text-sm">Sélectionner un joueur :</label>
                    <select className="w-full bg-gray-800 text-white text-lg rounded-lg p-2 border border-gray-600 mt-2" value={selectedPlayer} onChange={(e) => setSelectedPlayer(e.target.value)}>
                        {players.map(player => (<option key={player.name} value={player.name}>{player.name}</option>))}
                    </select>

                    <table className="w-full bg-white text-black rounded-lg overflow-hidden shadow-lg mt-4">
                        <thead className="bg-gray-200">
                            <tr>
                                <th className="p-2">Date & Heure</th>
                                <th className="p-2">Joueur 1</th>
                                <th className="p-2">Score</th>
                                <th className="p-2">Joueur 2</th>
                            </tr>
                        </thead>
                        <tbody>
                            {playerMatches.map((match, index) => {
                                const date = new Date(match.startTime);
                                const formattedDate = `${date.toLocaleDateString()} ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;
                                return (
                                    <tr key={index} className="text-center border-b">
                                        <td className="p-2">{formattedDate}</td>
                                        <td className="p-2">{match.opponent1}</td>
                                        <td className="p-2 font-bold">
                                            <table className="w-full border-collapse border border-gray-300 text-xs">
                                                <thead>
                                                    <tr className="border border-gray-300 bg-gray-200">
                                                        <td className="p-1 text-lg text-center" colSpan={3}>
                                                            {match.opponent1Point} - {match.opponent2Point}
                                                        </td>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr className="border border-gray-300">
                                                        <td className="p-1 font-bold text-left">⏱ Temps (sec)</td>
                                                        <td className="p-1 text-center">{match.opponent1totalTime}</td>
                                                        <td className="p-1 text-center">{match.opponent2totalTime}</td>
                                                    </tr>
                                                    <tr className="border border-gray-300">
                                                        <td className="p-1 font-bold text-left">⛔ Erreurs</td>
                                                        <td className="p-1 text-center">{match.opponent1errorCount}</td>
                                                        <td className="p-1 text-center">{match.opponent2errorCount}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                        <td className="p-2">{match.opponent2}</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </>
            )}
        </div>
    );
};

export default MatchPanel;
