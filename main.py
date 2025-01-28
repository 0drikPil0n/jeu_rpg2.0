import time
import random

def verifier_nom(p_prenom:str, p_nom:str) -> str:
    """
    Vérifie si le nom et le prénom sont correcte et retourne le nom complet
    :param p_prenom: Le prénom
    :param p_nom: Le nom de famille
    :return: Le nom complet
    """
    while not p_prenom.isalpha():
        p_prenom = input("Entrer un prénom correcte: ").capitalize()
    while not p_nom.isalpha():
        p_nom = input("Entrer un nom de famille correcte: ").capitalize()
    p_nom_complet = p_prenom + " " + p_nom

    return p_nom_complet



if __name__ == '__main__':
    # Choix du nom du personnage
    prenom: str = input("Veuillez entrer le prénom de votre personnage: ").capitalize()
    nom: str = input("Veuillez choisir votre nom de famille: ").capitalize()
    nom_complet = verifier_nom(prenom, nom)
