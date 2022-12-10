"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
# from api import débuter_partie, jouer_coup, lister_parties
from quoridor import Quoridor
# from utilitaire import analyser_commande, formater_les_parties

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "523d4f1b-6ca7-4879-9d15-40ff4fcbfb3b"

if __name__ == "__main__":
    joueurs = ["Player", "Robot"]
    game = Quoridor(joueurs)

    while not game.est_terminée():
        print(game)
        choice, pos = game.récupérer_le_coup(1)
        if choice == "D":
            game.déplacer_jeton(1, pos)
        else:
            game.placer_un_mur(1, pos, choice)
        if not game.est_terminée():
            game.jouer_le_coup(2)

    print(game)
    print(f"Congrats to {game.est_terminée()} for your incredible victory")


    # args = analyser_commande()
    # if args.parties:
    #     parties = lister_parties(args.idul, SECRET)
    #     print(formater_les_parties(parties))
    # else:
#     if args.local:

    # We might do pretty the same things as if we wanted to play
    # with a virtual bot, but we must consider to play player 1 and 2?

    # id_partie, état = débuter_partie(args.idul, SECRET)
    #     while True:
    #     # Afficher la partie
    #     print(formater_jeu(état))
    #     # Demander au joueur 1 de choisir son prochain coup
    #     type_coup, position = récupérer_le_coup()

        # Demander au joueur 2 de choisir son prochain coup


#     pass
# else:
    # When playing against the server bot. This is copy pasted from Proj1;
    # probably needs to be rewritten for OOP.

    # id_partie, état = débuter_partie(args.idul, SECRET)
    # while True:
    #     # Afficher la partie
    #     print(formater_jeu(état))
    #     # Demander au joueur de choisir son prochain coup
    #     type_coup, position = récupérer_le_coup()
    #     # Envoyez le coup au serveur
    #     id_partie, état = jouer_coup(
    #         id_partie,
    #         type_coup,
    #         position,
    #         args.idul,
    #         SECRET,
    #     )
