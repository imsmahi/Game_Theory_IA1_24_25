import json
import random

# Liste des joueurs (équipes)
players = [
    "Bekhechi-Hassain", "Belkhouche-Bouayed", "Mezouari", "Bouziani-Oudjedi",
    "Sabra", "Cherki-Maachou", "Belarbi-Belarbi", "Habi",
    "Benyelles", "Mekelleche", "Taibi", "Mekidiche",
    "Mekkaoui", "Smahi"
]

num_teams = len(players)  # 14 équipes
num_match_days = num_teams - 1  # 13 journées pour l'aller
match_schedule = []  # Stocker les matchs

# Générer un ordre aléatoire pour les journées
random.shuffle(players)

# 🔹 **Génération de la PHASE ALLER**
for day in range(1, num_match_days + 1):
    matches = []
    
    for i in range(num_teams // 2):
        team1 = players[i]
        team2 = players[num_teams - 1 - i]

        # Alternance domicile/extérieur
        if day % 2 == 0:
            team1, team2 = team2, team1

        matches.append({
            "matchDay": day,
            "startTime": "",
            "opponent1": team1,
            "opponent1Point": 0, "opponent1totalTime": 0, "opponent1errorCount": 0,
            "opponent2": team2,
            "opponent2Point": 0, "opponent2totalTime": 0, "opponent2errorCount": 0
        })

    match_schedule.extend(matches)

    # Rotation des équipes (sauf la première qui reste fixe)
    players = [players[0]] + [players[-1]] + players[1:-1]

# 🔄 **Génération de la PHASE RETOUR**
phase_retour = [
    {
        "matchDay": match["matchDay"] + 13,  # Décalage de 13 journées
        "startTime": "",
        "opponent1": match["opponent2"],  # Inversion domicile/extérieur
        "opponent1Point": 0, "opponent1totalTime": 0, "opponent1errorCount": 0,
        "opponent2": match["opponent1"],
        "opponent2Point": 0, "opponent2totalTime": 0, "opponent2errorCount": 0
    }
    for match in match_schedule
]

# Ajouter la phase retour au calendrier complet
match_schedule.extend(phase_retour)

# Sauvegarde du fichier JSON
with open("full_schedule.json", "w", encoding="utf-8") as file:
    json.dump(match_schedule, file, indent=4, ensure_ascii=False)

print(f"✅ Championnat complet généré avec {len(match_schedule)} matchs répartis sur 26 journées.")
