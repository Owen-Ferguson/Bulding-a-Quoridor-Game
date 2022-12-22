"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy

from quoridor_error import QuoridorError

from graphe import construire_graphe

import networkx as nx

class Quoridor():
    """Classe pour encapsuler le jeu Quoridor.
    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """

    def __init__(self, joueurs, murs=None):#DONT TOUCH
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))

    def vérification(self, joueurs, murs):
        """Initialization check of an instance of the Quoridor class.

        Validates the construction arguments of the instance and returns the state if valid.

        Args:
            joueurs (List): an iterable of two players, the first one always starts the game.
            murs (Dict, optionnel): 'horizontal' key associated with the list of [x, y]
                                    for horizontal wall positions,
                                    'vertical' key associated with the list of [x, y]
                                    for vertical wall positions.
        Returns:
            Dict: A copy of the current state of the game in the form of a dictionary.
            Note that the positions must be in the form of list [x, y] only.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """

        if not isinstance(joueurs, list):
        # if type(joueurs) != list:
            QuoridorError.wrong_player_type()
        if len(joueurs) != 2:
            QuoridorError.incorrect_player_number()

        #Initialize the state dictionary
        state = {}
        #Initialize the state variable with empty lists
        state["murs"] = {"horizontaux": [],
                        "verticaux": []}
        #Initialize the state given just the names; i.e. starting a new game
        if isinstance(joueurs[0], str):
            state["joueurs"] = [{"nom": joueurs[0], "murs": 10, "pos": [5,1]},\
                    {"nom": joueurs[1], "murs": 10, "pos": [5,9]}]

        #If the game is already defined, summarize the info here
        elif isinstance(joueurs[0], dict):

            #Error if the number of walls is invalid
            if 0 > joueurs[0]["murs"] or joueurs[0]["murs"] > 10 or\
                joueurs[1]["murs"] < 0 or joueurs[1]["murs"] > 10:
                QuoridorError.incorrect_wall_number()

            #Error if the player position is invalid
            for i in range(2):
                if 1 > joueurs[0]["pos"][i] or joueurs[0]["pos"][i] > 9\
                    or 1 > joueurs[1]["pos"][i] or  joueurs[1]["pos"][i] > 9:
                    QuoridorError.invalid_player_position()

            state["joueurs"] = [{"nom": joueurs[0]["nom"], "murs": joueurs[0]["murs"],\
                   "pos": joueurs[0]["pos"]}, {"nom": joueurs[1]["nom"],\
                    "murs": joueurs[1]["murs"], "pos": joueurs[1]["pos"]}]

        #If no walls dict given, the total walls must still be equal to 20
        if not murs:
            if state["joueurs"][0]["murs"] + state["joueurs"][1]["murs"] != 20:
                QuoridorError.invalid_wall_count()

        elif murs:
            #Dealing with more errors
            if not isinstance(murs, dict):
                QuoridorError.walls_invalid_type()

            #Add the walls info to the final dictionary
            state["murs"]["horizontaux"] = murs["horizontaux"]
            state["murs"]["verticaux"] = murs["verticaux"]

            if state["joueurs"][0]["murs"] + state["joueurs"][1]["murs"]\
                + len(state["murs"]["horizontaux"]) + len(state["murs"]["verticaux"]) != 20:
                QuoridorError.invalid_wall_count()

            #Last error check to make sure that the walls are in valid places
            for wall in state["murs"]["horizontaux"]:
                if wall[0] < 1 or wall[0] > 8 or wall[1] < 2 or wall[1] > 9:
                    QuoridorError.invalid_wall_placement()
            for wall in state["murs"]["verticaux"]:
                if wall[0] < 2 or wall[0] > 9 or wall[1] < 1 or wall[1] > 8:
                    QuoridorError.invalid_wall_placement()

        return state

    def formater_légende(self):
        """Formater la représentation graphique de la légende.

        Returns:
            str: Chaîne de caractères représentant la légende.
        """
        #Take the state from the instance variable

        joueurs = self.état["joueurs"]

        #Start writing out the names
        p1_name = joueurs[0]['nom'] + ","
        p2_name = joueurs[1]['nom'] + ","

        #Add spaces to the shorter name (if it's shorter) for alignment
        size = max(len(p1_name), len(p2_name))
        if len(p1_name) != size:
            p1_name += ((size) - len(p1_name))*' '
        elif len(p2_name) != size:
            p2_name += ((size) - len(p2_name))*' '

        p1_murs = joueurs[0]['murs']*"|" + "\n"
        p2_murs = joueurs[1]['murs']*"|" + "\n"

        final_string = "Légende:\n" + "   1=" + p1_name + " murs=" \
            + p1_murs + "   2=" + p2_name + " murs=" + p2_murs

        return final_string

    def formater_damier(self):
        """Formater la représentation graphique du damier.
        Args:
            joueurs (list): Liste de dictionnaires représentant les joueurs.
            murs (dict): Dictionnaire représentant l'emplacement des murs.
        Returns:
            str: Chaîne de caractères représentant le damier.
        """
        #Affiche le tableau de jeu vide
        joueurs = self.état['joueurs']
        murs = self.état['murs']
        board = [["   " + "-" * 35],
                ["9 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["8 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["7 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["6 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["5 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["4 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["3 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["2 " + "| " + ".   " * 8 + ". |"],
                ["  " + "|" + " "* 34 + " |"],
                ["1 " + "| " + ".   " * 8 + ". |"],
                ["--" + "|" + "-"* 35],
                ["  " + "| "+"1   "+"2   "+"3   "+"4   "+"5   "+"6   "+"7   "+"8   "+"9"]
                ]

        pos_player1 = joueurs[0]['pos']
        pos_player2 = joueurs[1]['pos']
        #on determine la constante qui nous permettra de traduire
        #le numéro de position indiqué sur le display
        #vers la ligne réelle du board: y=ax+b
        #où a correspond a la pente, i.e à chaque fois qu'on descend d'un numéro d'afficher,
        #et b correspond au offset, i.e quel numéro de ligne on cherche à traduire
        #x correspond à l'élément de board[i] auquel on cherche à accéder
        #Pour l'équation en colonne: y = 4x

        #Determine la position pour chaque joueur
        corresp_row_p1 = int((-2 * pos_player1[1]) + 19)
        corresp_row_p2 = int((-2 * pos_player2[1]) + 19)

        corresp_col_p1 = int(4 * pos_player1[0])
        corresp_col_p2 = int(4 * pos_player2[0])

        #Dans le cas où 2 joueurs sont sur la même ligne
        if pos_player1[1] == pos_player2[1]:
            if pos_player1[0] == pos_player2[0]:
                raise Exception("Un joueur est déjà présent à cet emplacement!")
            modif_row1 = [list(str(pos_player1[1]) + " |" + 8 * " .  " + " . " + "|")]
            modif_row1[0][corresp_col_p1] = "1"
            modif_row1[0][corresp_col_p2] = "2"
            final_row1 = [''.join([str(elem) for elem in modif_row1[0]])]
            board[corresp_row_p1] = final_row1

        #Dans le cas où les 2 joueurs sont sur différentes lignes
        else:
            modif_row1 = [list(str(pos_player1[1]) + " |" + 8 * " .  " + " . " + "|")]
            modif_row1[0][corresp_col_p1] = "1"
            modif_row2 = [list(str(pos_player2[1]) + " |" + 8 * " .  " + " . " + "|")]
            modif_row2[0][corresp_col_p2] = "2"

            final_row1 = [''.join([str(elem) for elem in modif_row1[0]])]
            final_row2 = [''.join([str(elem) for elem in modif_row2[0]])]

            board[corresp_row_p1] = final_row1
            board[corresp_row_p2] = final_row2

        #Maintenant, on affiche les murs.
        #1- les murs horizontaux
        murs_horiz = murs["horizontaux"]
        for mur in murs_horiz:
            if 0 > mur[0] > 9 or 1 > mur[1] > 10:
                raise Exception("Coordonnées invalides pour placer le mur")
            mur_coord = mur
            mur_row = int(-2* mur_coord[1] + 20)
            mur_col = 4 * mur_coord[0] - 1

            if "-" in board[mur_row][0][mur_col:mur_col+7]:
                raise Exception("Il y a déjà un mur ici!")

        #Réecris la ligne si pas déjà affichée avant
            if "-" not in board[mur_row][0][mur_col:mur_col+7]:
                new_row_mur1 = [list(board[mur_row][0])]
                new_row_mur1[0][mur_col:mur_col+7] = "-------"
                new_row_mur1 = [''.join([str(elem) for elem in new_row_mur1[0]])]
                board[mur_row] = new_row_mur1

        #2- les murs verticaux
        murs_verti = murs["verticaux"]
        for mur in murs_verti:
            if 0 > mur[0] > 9 or 1 > mur[1] > 10:
                raise Exception("Coordonnées invalides pour placer le mur")
            mur_coord = mur

            mur_row1 = int(-2* mur_coord[1] + 19)
            #3 lignes que prend le mur vertical
            murs_verti_coord = [mur_row1, mur_row1 - 1, mur_row1 - 2]
            mur_col = 4 * mur_coord[0] - 2

            for mur2 in murs_verti_coord:
                final_row = list(board[mur2][0])
                final_row[mur_col] = "|"
                final_row = [''.join([str(elem) for elem in final_row])]
                board[mur2] = final_row

        #This line pour enlever les crochets autour des éléments
        new_board = '\n'.join(' '.join(sub) for sub in board)
        return new_board + '\n'

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.
        Cette représentation est la même que celle du projet précédent.
        Returns:
            str: La chaîne de caractères de la représentation.
        """

        lgd = self.formater_légende()
        brd = self.formater_damier()

        return lgd + brd

    def état_courant(self):#DONT TOUCH
        """Produire l'état actuel du jeu.
        Cette méthode ne doit pas être modifiée.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)

    def est_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        #Need to add first in the dictionnary the new key "gagnant" = None
        state = self.état
        joueurs = state["joueurs"]

        #Returns true when a player reaches the opposite side of the board; else false
        if joueurs[0]['pos'][1]== 9:
            return joueurs[0]["nom"]

        if joueurs[1]['pos'][1] == 1:
            return joueurs[1]["nom"]

        return False


    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
        """
        if joueur in (1, 2):
            type_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):")
            if type_coup not in ['D','MH','MV']:
                return QuoridorError.wrong_type_move()

            position = input("Donnez la position où appliquer ce coup (x,y):")
            a = position.split(",")
            #Convert this list of strings to a list of integers
            position = [int(i) for i in a]
            x, y = position[0], position[1]
            if 1 > x or x > 9 or 1 > y or y > 9:
                return QuoridorError.out_of_game_position()

            return (type_coup, [int(position[0]),int(position[1])])

        QuoridorError.incorrect_p_number_assigned()
        return None

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.
        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """

        #If the number given does not match 1 or 2:
        if joueur not in (1, 2):
            QuoridorError.incorrect_p_number_assigned()

        #If the given position is outside the limitation of the board:
        x, y = position[0], position[1]
        if 1 > x or x > 9 or 1 > y or y > 9:
            QuoridorError.out_of_game_position()

        state = self.état

        graphe = construire_graphe(
            [joueur['pos'] for joueur in state['joueurs']],
            state['murs']['horizontaux'],
            state['murs']['verticaux']
        )

        valid = list(graphe.successors(tuple(state["joueurs"][joueur - 1]['pos'])))

        if tuple(position) not in valid:
            QuoridorError.invalid_pos_current_game()

        state["joueurs"][joueur - 1]['pos'] = position

        return state

    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.
        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """


        state = self.état

        if orientation == "MH":
            orientation = "horizontaux"
        if orientation == "MV":
            orientation = "verticaux"

        if joueur not in (1, 2):
            QuoridorError.incorrect_p_number_assigned()
        if position in state["murs"][orientation]:
            QuoridorError.wall_already_here()

        #Error when placing overlapping walls
        if orientation == "horizontaux":
            for i in state['murs']['horizontaux']:
                if i[1] == position[1]:
                    if i[0] == (position[0] + 1) or\
                        i[0] == (position[0] - 1):
                        QuoridorError.wall_already_here()


        if orientation == "verticaux":
            for i in state['murs']['verticaux']:
                if i[0] == position[0]:
                    if i[1] == (position[1] + 1) or\
                        i[1] == (position[1] - 1) or\
                        i[1] == position[1]:
                        QuoridorError.wall_already_here()


        # Error when placing overlapping horizontal and vertical walls
        if orientation == "verticaux":
            for i in state['murs']['horizontaux']:
                if i[0] == (position[0] - 1) and\
                    i[1] == (position[1] + 1):
                    QuoridorError.wall_already_here()


        if orientation == "horizontaux":
            for i in state['murs']['verticaux']:
                if i[0] == (position[0] - 1) and\
                    i[1] == (position[1] + 1):
                    QuoridorError.wall_already_here()


        #Error 3(1) If the given position is outside the limitation of the board:
        x, y = position[0], position[1]
        if 1 > x or x > 9 or 1 > y or y > 9:
            QuoridorError.incorrect_wall_orientation()


        if state["joueurs"][joueur - 1]["murs"] < 1:
            QuoridorError.no_more_walls()

        state["murs"][orientation].append(position)

        graphe = construire_graphe(
            [joueur['pos'] for joueur in state['joueurs']],
            state['murs']['horizontaux'],
            state['murs']['verticaux']
        )

        #Error if the player block themselves in
        if not nx.has_path(graphe, tuple(state["joueurs"][joueur - 1]["pos"]), 'B' + str(joueur)):
            state["murs"][orientation].remove(position)
            QuoridorError.incorrect_wall_orientation()

        # Error if the player blocks the other player in
        if joueur == 1:
            if not nx.has_path(graphe, tuple(state["joueurs"][1]["pos"]), 'B2'):
                state["murs"][orientation].remove(position)
                QuoridorError.incorrect_wall_orientation()
        if joueur == 2:
            if not nx.has_path(graphe, tuple(state["joueurs"][0]["pos"]), 'B1'):
                state["murs"][orientation].remove(position)
                QuoridorError.incorrect_wall_orientation()

        state["joueurs"][joueur - 1]["murs"] -= 1

        return state


    def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.

        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        if joueur not in (1, 2):
            QuoridorError.incorrect_p_number_assigned()

        # if self.est_terminée() is not False:
        #     QuoridorError.end_of_the_game()

        state = self.état

        graphe = construire_graphe(
            [joueur['pos'] for joueur in state['joueurs']],
            state['murs']['horizontaux'],
            state['murs']['verticaux']
        )

        #TODO To make this automatic play a bit smarter, we are going to take several steps:
        '''
        1. Check the length of the shortest path for each player
        2a.       if our path is shorter, make a move in the shortest path
        2b.       if their path is shorter, place a wall
        3.        if wall, then place it in the way of their shortest path
            For that, we can either test a bunch of placements, calculate the number of
            steps it added for the opponent, and place the most effective wall,

            OR

            We can test a few walls in different orientations in an area around the other players
            next move, and place the first wall that adds at least 2 steps to their shortest path

            Option 1 will win us more games, but we won't do it if the processing time is too long
            This I'm not so sure of; will it take too long? We want less than ~5 seconds per turn.

        '''

        shortest_p1 = nx.shortest_path(graphe, tuple(state["joueurs"][0]["pos"]), 'B1')
        shortest_p2 = nx.shortest_path(graphe, tuple(state["joueurs"][1]["pos"]), 'B2')

        if len(shortest_p1) <= len(shortest_p2) or state['joueurs'][0]['murs'] == 0:
            next_step_p1 = shortest_p1[1]
            return("D", next_step_p1)

        else:
            def temp_wall(x, y, orientation):
                if x >= 1 and x <= 9 and y >=1 and y <= 9:
                    try:
                        self.placer_un_mur(1, (x, y), orientation)
                    except:
                        return


            def remove_temp_wall(x, y, orientation):
                #No if statements required here for error coverage; 
                #we only call the function after placing a temp wall
                if orientation == "MH":
                    if (x, y) in state['murs']['horizontaux']:
                        state['murs']['horizontaux'].remove((x, y))
                        state["joueurs"][joueur - 1]["murs"] += 1
                if orientation == "MV":
                    if (x,y) in state['murs']['verticaux']:
                        state['murs']['verticaux'].remove((x, y))
                        state["joueurs"][joueur - 1]["murs"] += 1


            path_length = []
            shortest_p2 = shortest_p2[:-1]
            to_remove = []

            for point in shortest_p2:
                if point in state['murs']['horizontaux'] or point in state['murs']['verticaux']:
                    to_remove.append(point)

            for removal in to_remove:
                if removal in shortest_p2:
                    shortest_p2.remove(removal)

            for i in range(len(shortest_p2)): 
                #The size of this list will change below; not sure if it will affect the loop
                #Add a horizontal temp wall, determine the length of the P2 shortest path, 
                #remove it, repeat with vertical
                #Check if the temp wall will be out of bounds
                #print(state['murs']['horizontaux'], [shortest_p2[i][0], shortest_p2[i][1]])
                if shortest_p2[i][0] >= 1 and shortest_p2[i][0] < 9 and shortest_p2[i][1] <= 9 and\
                shortest_p2[i][1] > 1:
                    if [shortest_p2[i][0], shortest_p2[i][1]] in state['murs']['horizontaux'] or\
                        [shortest_p2[i][0] - 1, shortest_p2[i][1]] in\
                        state['murs']['horizontaux'] or\
                        [shortest_p2[i][0] + 1, shortest_p2[i][1]] in\
                        state['murs']['horizontaux']:
                        pass
                    elif [shortest_p2[i][0], shortest_p2[i][1]] in state['murs']['verticaux'] or\
                         [shortest_p2[i][0] + 1, shortest_p2[i][1]] in state['murs']['verticaux']:
                        pass
                    else:
                        temp_wall(shortest_p2[i][0], shortest_p2[i][1], "MH")
                        new_shortest_p2 = nx.shortest_path(graphe\
                        , tuple(state["joueurs"][1]["pos"]), 'B2')
                        path_length.append(("MH", (shortest_p2[i][0], shortest_p2[i][1])\
                        , len(new_shortest_p2)))
                        remove_temp_wall(shortest_p2[i][0], shortest_p2[i][1], "MH")

            for i in range(len(shortest_p2)):
                if shortest_p2[i][0] > 1 and shortest_p2[i][0] < 9 and\
                shortest_p2[i][1] > 1 and shortest_p2[i][1] < 9:
                    if [shortest_p2[i][0], shortest_p2[i][1]] in state['murs']['verticaux'] or\
                    [shortest_p2[i][0], shortest_p2[i][1] + 1] in state['murs']['verticaux'] or\
                    [shortest_p2[i][0], shortest_p2[i][1] - 1] in state['murs']['verticaux']:
                        pass
                    elif [shortest_p2[i][0], shortest_p2[i][1]] in state['murs']['horizontaux']\
                    or [shortest_p2[i][0], shortest_p2[i][1] + 1] in state['murs']['horizontaux']:
                        pass
                    else:
                        temp_wall(shortest_p2[i][0], shortest_p2[i][1], "MV")
                        new_shortest_p2 = nx.shortest_path(graphe, tuple(state["joueurs"][1]["pos"]), 'B2')
                        path_length.append(("MV", (shortest_p2[i][0], shortest_p2[i][1])\
                        , len(new_shortest_p2)))
                        remove_temp_wall(shortest_p2[i][0], shortest_p2[i][1], "MV")

            for i in range(len(shortest_p2)):
                if shortest_p2[i][0] == 9 and shortest_p2[i][1] < 9 and shortest_p2[i][1] > 1:
                    temp_wall(shortest_p2[i][0] - 1, shortest_p2[i][1], "MH")
                    path_length.append(("MH", (shortest_p2[i][0] - 1, shortest_p2[i][1])\
                        , len(shortest_p2)))
                    remove_temp_wall(shortest_p2[i][0] - 1, shortest_p2[i][1], "MH")

            #This line returns the element of the list that adds the largest number of steps for p2.
            #If there is no good wall placement, it moves the player
            #If there are multiple options, it still only returns 1 which is fine
            if path_length == []:
                best_move = ("D", shortest_p1[1])
            else:
                best_move = max(path_length, key=lambda x:x[2])

            #This will return something like ("MH", (2, 2))
            return(best_move[0], (best_move[1][0], best_move[1][1]))

        ###################################################################################
        #Can uncomment the lines below here to make the simple version of the code work
       #next_step = nx.shortest_path(graphe, tuple(state["joueurs"][joueur - 1]["pos"]),\
        #    'B' + str(joueur))

        #return ("D", next_step[1])
