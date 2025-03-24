import json
import os

# 📂 Chemins des fichiers JSON
PLAYERS_FILE = "players.json"
MATCHES_FILE = "matches.json"
OUTPUT_FILE = "championship.html"

# 🛠 Vérification des fichiers JSON
if not os.path.exists(PLAYERS_FILE):
    print(f"🚨 ERREUR: {PLAYERS_FILE} introuvable !")
    exit(1)
if not os.path.exists(MATCHES_FILE):
    print(f"🚨 ERREUR: {MATCHES_FILE} introuvable !")
    exit(1)

# 📥 Chargement des données JSON
with open(PLAYERS_FILE, "r", encoding="utf-8") as f:
    players = json.load(f)

with open(MATCHES_FILE, "r", encoding="utf-8") as f:
    matches = json.load(f)

# 🏆 Génération du classement
for player in players:
    player.setdefault("points", 0)
    player.setdefault("wins", 0)
    player.setdefault("losses", 0)
    player.setdefault("draws", 0)
    player.setdefault("totalTime", 0)
    player.setdefault("totalErrors", 0)

# 🔢 Tri du classement par points (puis temps total et erreurs)
players_sorted = sorted(
    players,
    key=lambda p: (-p["points"], p["totalTime"], p["totalErrors"])
)

# 🎯 Récupération des journées disponibles
match_days = sorted(set(match["matchDay"] for match in matches))

# 📜 Génération du tableau des matchs par journée
matches_by_day = {
    day: [match for match in matches if match["matchDay"] == day] for day in match_days
}

match_tables = {}
for day, day_matches in matches_by_day.items():
    match_tables[day] = "\n".join(
        f'<tr><td>{match["startTime"]}</td><td>{match["opponent1"]}</td>'
        f'<td class="bold">{match["opponent1Point"]} - {match["opponent2Point"]}</td>'
        f'<td>{match["opponent2"]}</td></tr>'
        for match in day_matches
    )

# 🎯 Génération du tableau du classement
ranking_table = "\n".join(
    f'<tr><td>{i+1}</td><td>{p["name"]}</td><td>{p["points"]}</td>'
    f'<td>{p["wins"] + p["losses"] + p["draws"]}</td><td>{p["wins"]}</td>'
    f'<td>{p["losses"]}</td><td>{p["draws"]}</td>'
    f'<td>{p["totalTime"]} sec</td><td>{p["totalErrors"]}</td></tr>'
    for i, p in enumerate(players_sorted)
)

# 🖥 Création de la page HTML
html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Championnat</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; }}
        h1 {{ color: #333; }}
        .container {{ max-width: 900px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #aaa; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: center; }}
        th {{ background-color: #333; color: white; }}
        .bold {{ font-weight: bold; font-size: 18px; }}
        select {{ padding: 10px; margin: 10px 0; }}
    </style>
    <script>
        function showMatches() {{
            var selectedDay = document.getElementById("daySelect").value;
            document.querySelectorAll(".matchTable").forEach(table => table.style.display = "none");
            document.getElementById("matches_" + selectedDay).style.display = "table";
        }}
    </script>
</head>
<body>
    <div class="container">
        <h1>🏆 Championnat Tic-Tac-Toe</h1>

        <h2>📅 Sélectionner une journée</h2>
        <select id="daySelect" onchange="showMatches()">
            {"".join(f'<option value="{day}">Journée {day}</option>' for day in match_days)}
        </select>

        <h2>📋 Liste des matchs</h2>
        {"".join(f'<table id="matches_{day}" class="matchTable" style="display:none;"><tr><th>Date</th><th>Joueur 1</th><th>Score</th><th>Joueur 2</th></tr>{match_tables[day]}</table>' for day in match_days)}

        <h2>🏅 Classement</h2>
        <table>
            <tr>
                <th>Position</th>
                <th>Joueur</th>
                <th>Points</th>
                <th>Joués</th>
                <th>Gagnés</th>
                <th>Perdus</th>
                <th>Nuls</th>
                <th>Temps</th>
                <th>Erreurs</th>
            </tr>
            {ranking_table}
        </table>
    </div>

    <script>
        document.getElementById("daySelect").value = "{match_days[0]}";
        showMatches();
    </script>
</body>
</html>"""

# 💾 Écriture dans un fichier HTML
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Fichier HTML généré avec succès : {OUTPUT_FILE}")
