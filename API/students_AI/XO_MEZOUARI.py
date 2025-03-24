import itertools
import time
from functools import lru_cache

JOUEUR_X, JOUEUR_O, VIDE = "X", "O", None
PROFONDEUR_MAX = 6  # Définir une profondeur maximale pour l'exploration

def etat_initial():
    return (("X", "X", "O"), ("O", "O", VIDE), ("X", VIDE, VIDE))

def est_terminal(plateau):
    return gagnant(plateau) is not None or all(cell is not VIDE for row in plateau for cell in row)

def gagnant(plateau):
    for joueur in (JOUEUR_X, JOUEUR_O):
        if (
            any(all(cell == joueur for cell in ligne) for ligne in plateau) or
            any(all(plateau[r][c] == joueur for r in range(3)) for c in range(3)) or
            all(plateau[i][i] == joueur for i in range(3)) or
            all(plateau[i][2 - i] == joueur for i in range(3))
        ):
            return joueur
    return None

def actions_possibles(plateau):
    return [(r, c) for r, c in itertools.product(range(3), repeat=2) if plateau[r][c] == VIDE]

def appliquer_action(plateau, action, joueur):
    r, c = action
    return tuple(
        tuple(cell if (i, j) != (r, c) else joueur for j, cell in enumerate(ligne))
        for i, ligne in enumerate(plateau)
    )

def evaluation_heuristique(plateau):
    """ Évalue l’état du plateau avec une heuristique simple. """
    score = 0
    lignes = list(plateau) + [tuple(plateau[r][c] for r in range(3)) for c in range(3)]
    lignes.append(tuple(plateau[i][i] for i in range(3)))  # Diagonale principale
    lignes.append(tuple(plateau[i][2 - i] for i in range(3)))  # Diagonale secondaire

    for ligne in lignes:
        if ligne.count(JOUEUR_X) == 3:
            return 10
        elif ligne.count(JOUEUR_O) == 3:
            return -10
        elif ligne.count(JOUEUR_X) == 2 and ligne.count(VIDE) == 1:
            score += 1
        elif ligne.count(JOUEUR_O) == 2 and ligne.count(VIDE) == 1:
            score -= 1

    return score

@lru_cache(None)
def minimax(plateau, joueur_actuel, profondeur=0, alpha=float('-inf'), beta=float('inf')):
    if est_terminal(plateau):
        gagnant_partie = gagnant(plateau)
        if gagnant_partie == JOUEUR_X:
            return 10 - profondeur, None
        elif gagnant_partie == JOUEUR_O:
            return profondeur - 10, None
        return 0, None  # Match nul

    if profondeur >= PROFONDEUR_MAX:
        return evaluation_heuristique(plateau), None

    coups = actions_possibles(plateau)
    coups.sort(key=lambda action: evaluation_heuristique(appliquer_action(plateau, action, joueur_actuel)), reverse=True)

    if joueur_actuel == JOUEUR_X:
        meilleur_score, meilleur_coup = float("-inf"), None
        for action in coups:
            score, _ = minimax(appliquer_action(plateau, action, JOUEUR_X), JOUEUR_O, profondeur + 1, alpha, beta)
            if score > meilleur_score:
                meilleur_score, meilleur_coup = score, action
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return meilleur_score, meilleur_coup
    else:
        pire_score, pire_coup = float("inf"), None
        for action in coups:
            score, _ = minimax(appliquer_action(plateau, action, JOUEUR_O), JOUEUR_X, profondeur + 1, alpha, beta)
            if score < pire_score:
                pire_score, pire_coup = score, action
            beta = min(beta, score)
            if alpha >= beta:
                break
        return pire_score, pire_coup

debut = time.time()
plateau = etat_initial()
_, meilleur_coup = minimax(plateau, JOUEUR_X)
fin = time.time()

print("Meilleur coup pour X :", meilleur_coup)
print(f"Temps : {fin - debut:.6f} secondes")
