import time
import random
carte = {0:["T","Z","T","T","T","T","T","T","T","F"],
         1:["T","T","T","T","T","T","T","T","T","T"],
         2:["T","T","T","T","T","T","T","T","T","T"],
         3:["T","T","T","T","T","T","T","T","T","T"],
         4:["T","T","T","T","T","T","H","T","T","T"],
         5:["T","T","T","T","T","T","T","T","T","T"],
         6:["T","T","T","T","T","T","T","T","T","T"],
         7:["T","T","T","T","T","T","T","T","T","T"],
         8:["T","T","T","T","T","T","T","T","T","T"],
         9:["K","T","T","T","T","T","T","T","B","T"],}
def position_depart(map_):
    """
    Choisis la position de départ du joueur sur la carte
    :param map_: La carte
    :return: La position du joueur sur la carte
    """
    # Initialize les variable
    p_position_depart = None
    hauteur = None
    largeur = None
    while p_position_depart != "K":
        hauteur = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        largeur = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        p_position_depart = map_[hauteur][largeur]
    p_co_x = largeur + 1
    p_co_y = -(hauteur + 1) + 11

    return p_position_depart, int(p_co_y), int(p_co_x)

if __name__ == '__main__':
    position, co_y, co_x = position_depart(carte)
    print(carte)
