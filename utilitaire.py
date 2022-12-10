"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""

import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a trois attributs: « idul » représentant l'idul
                    du joueur, « parties » qui est un booléen `True`/`False`
                    et « local » qui est un booléen `True`/`False`.
    """

    parser = argparse.ArgumentParser(description="Quoridor")

    parser.add_argument('--idul', type=str, help='IDUL du joueur')
    parser.add_argument('--local-arg', action="store_true", default=False)
    parser.add_argument("-p", "--parties", help="List the existing parts",
                    action="store_true")
    return parser.parse_args()


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.
    Args:
        parties (list): Liste des parties
    Returns:
        str: Représentation des parties
    """
    summary = ''
    for ind, info in enumerate(parties):
        summary += f"{ind + 1} : {info['date']},\
            {info['joueurs'][0]} vs {info['joueurs'][1]}\n"

    return summary[:-1]
