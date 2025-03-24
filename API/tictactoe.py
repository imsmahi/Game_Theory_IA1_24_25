import random

from students_AI import XO_HASSAIN as ttt_Hassain
from students_AI import XO_BELKHOUCHE as ttt_Belkhouche
#from students_AI import XO_MEZOUARI as ttt_Mezouari
from students_AI import XO_OUDJEDI as ttt_Oudjedi
from students_AI import XO_SABRA as ttt_Sabra
from students_AI import XO_MAACHOU as ttt_Maachou
from students_AI import XO_BELARBI as ttt_Belarbi
from students_AI import XO_HABI as ttt_Habi
from students_AI import XO_BENYELLES as ttt_Benyelles
from students_AI import XO_MEKELLECHE as ttt_Mekelleche
from students_AI import XO_MEKIDECH as ttt_Mekidech
from students_AI import XO_MEKKAOUI as ttt_Mekkaoui
from students_AI import XO_TAIBI as ttt_Taibi
from students_AI import XO_SMAHI as ttt_Smahi




X = "X"
O = "O"
EMPTY = ""



# Take board state as List of List contain 3 Rows and 3 Columns
# Example of initial state board :
# board = 
# [     
#       [EMPTY, EMPTY, EMPTY],
#       [EMPTY, EMPTY, EMPTY],
#       [EMPTY, EMPTY, EMPTY]
# ]
#
# board can take 3 values (X,O,EMPTY)


def get_minimax_function(player_x):
    player_map = {
        "Bekhechi-Hassain": ttt_Hassain.minimax,
        "Belarbi-Belarbi": ttt_Belarbi.minimax2,
        "Belkhouche-Bouayed": ttt_Belkhouche.get_best_move,
        "Benyelles": ttt_Benyelles.best_move,
        "Bouziani-Oudjedi": ttt_Oudjedi.minimax,
        "Cherki-Maachou": ttt_Maachou.minimax1,
        "Habi": ttt_Habi.minimax2,        
        "Mekelleche": ttt_Mekelleche.minimax1,
        "Mekidiche": ttt_Mekidech.minimax2,
        "Mekkaoui": ttt_Mekkaoui.minimax1,
        #"Mezouari": ttt_Mezouari.minimax2,
        "Sabra": ttt_Sabra.minimax1,
        "Smahi": ttt_Smahi.minimax_,
        "Taibi": ttt_Taibi.bestMove        
    }
    
    return player_map.get(player_x, None)  # Retourne None si le joueur n'est pas trouvé

def minimax1(board, player,player_x):
    minimax_function = get_minimax_function(player_x)
    if minimax_function:
        return minimax_function(board, player)
    else:
        raise ValueError(f"Aucune fonction minimax trouvée pour le joueur: {player_x}")
    


def minimax2(board, player,player_o):
    minimax_function = get_minimax_function(player_o)
    if minimax_function:
        return minimax_function(board, player)
    else:
        raise ValueError(f"Aucune fonction minimax trouvée pour le joueur: {player_o}")
    