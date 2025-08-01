"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
import turtle
from api import débuter_partie, jouer_coup
from quoridor import Quoridor
from utilitaire import analyser_commande
from quoridorx import QuoridorX

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "87877acb-c834-4725-a127-61634c821053"

if __name__ == "__main__":
    args = analyser_commande()

    if args.automatique and args.graphique:

        #Play auto against server with GUI
        turtle.screensize(canvwidth=400, canvheight=400, bg="gainsboro")

        joueurs = []
        id_partie, ini_dic = débuter_partie(args.idul, SECRET)
        #Play automatically against the server without the GUI
        for i in range(2):
            joueurs.append(ini_dic['joueurs'][i]['nom'])

        game = QuoridorX(joueurs)

        while not game.est_terminée():

            choice, position = game.jouer_le_coup(1) #Make manual decision

            id_partie, new_state = jouer_coup(
                id_partie,
                choice,
                position,
                args.idul,
                SECRET,
                )

            game = QuoridorX(new_state['état']['joueurs'], new_state['état']['murs'])


        print(f"Congrats to {game.est_terminée()} for your incredible victory")
        game.gui()
        turtle.exitonclick()

    elif args.graphique:
        #Play manually against the server with GUI
        ####################################################################
        turtle.screensize(canvwidth=400, canvheight=400, bg="gainsboro")

        joueurs = []
        id_partie, ini_dic = débuter_partie(args.idul, SECRET)
        #Play automatically against the server without the GUI
        for i in range(2):
            joueurs.append(ini_dic['joueurs'][i]['nom'])

        game = QuoridorX(joueurs)

        while not game.est_terminée():

            game.gui()
            choice, position = game.récupérer_le_coup(1) #Make manual decision

            id_partie, new_state = jouer_coup(
                id_partie,
                choice,
                position,
                args.idul,
                SECRET,
                )

            game = QuoridorX(new_state['état']['joueurs'], new_state['état']['murs'])

        print(f"Congrats to {game.est_terminée()} for your incredible victory")
        game.gui()
        ####################################################################


    elif args.automatique:
        joueurs = []
        id_partie, ini_dic = débuter_partie(args.idul, SECRET)
        #Play automatically against the server without the GUI
        for i in range(2):
            joueurs.append(ini_dic['joueurs'][i]['nom'])

        game = Quoridor(joueurs)

        while not game.est_terminée():
            print(game)
            choice, position = Quoridor.jouer_le_coup(game, 1) #Auto play my move
            # choice, position = game.récupérer_le_coup(1)

            id_partie, new_state = jouer_coup(
                id_partie,
                choice,
                position,
                args.idul,
                SECRET,
             )
            print(new_state)
            game = Quoridor(new_state['état']['joueurs'], new_state['état']['murs'])

        print(game)
        print(f"Congrats to {game.est_terminée()} for your incredible victory")



    else:
        #play manually against the server without GUI
        joueurs = []
        id_partie, ini_dic = débuter_partie(args.idul, SECRET)
        #Play automatically against the server without the GUI
        for i in range(2):
            joueurs.append(ini_dic['joueurs'][i]['nom'])

        game = Quoridor(joueurs)

        while not game.est_terminée():
            print(game)
            choice, position = game.récupérer_le_coup(1) #Make manual decision

            id_partie, new_state = jouer_coup(
                id_partie,
                choice,
                position,
                args.idul,
                SECRET,
             )

            game = Quoridor(new_state['état']['joueurs'], new_state['état']['murs'] )

        print(game)
        print(f"Congrats to {game.est_terminée()} for your incredible victory")
