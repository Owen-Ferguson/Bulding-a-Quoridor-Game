"""Quoridor Error module

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
class QuoridorError(Exception):
    '''words words words'''
    def __init__(self, *args):
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f"{self.message}"

    def wrong_player_type(self=None):
        """Mauvaise entrée pour le numéro de joueur.
        Raise:
        QuoridorError: L'argument 'joueurs' n'est pas itérable.
            """
        raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")

    def incorrect_player_number(self=None):
        """Aucun des numéros de joueurs ne correspond.
        Raise:
        QuoridorError: L'itérable de joueurs contient un nombre différent de deux.
            """
        raise QuoridorError("L'itérable de joueurs contient un nombre différent de deux.")

    def incorrect_wall_number(self=None):
        """Nombre de murs supérieurs à 10 ou négatif.
        Raise:
        QuoridorError: Le nombre de murs qu'un joueur peut placer est plus
        grand que 10, ou négatif.
            """
        raise QuoridorError(''.join(("Le nombre de murs qu'un joueur peut placer",
            " est plus grand que 10, ou négatif.")))

    def invalid_player_position(self=None):
        """Position entrée pour le joueur est incorrecte
        Raise:
        QuoridorError: La position d'un joueur est invalide.
            """
        raise QuoridorError("La position d'un joueur est invalide.")

    def walls_invalid_type(self=None):
        """L'argument 'murs' n'est pas un dictionnaire lorsque présent.
        Raise:
        QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            """
        raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")

    def invalid_wall_count(self=None):
        """Le total des murs placés et plaçables n'est pas égal à 20.
        Raise:
        QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            """
        raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20.")

    def invalid_wall_placement(self=None):
        """Position du mur donnée est invalide.
        Raise:
        QuoridorError: La position d'un mur est invalide.
            """
        raise QuoridorError("La position d'un mur est invalide.")

    def incorrect_p_number_assigned(self=None):
        """Numéro de joueur différent de 1 ou 2.
        Raise:
        QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            """
        raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")

    def out_of_game_position(self=None):
        """Position donnée hors du damier.
        Raise:
        QuoridorError: La position est invalide (en dehors du damier).
            """
        raise QuoridorError("La position est invalide (en dehors du damier).")

    def invalid_pos_current_game(self=None):
        """La position est invalide pour l'état actuel du jeu.
        Raise:
        QuoridorError: La position est invalide (en dehors du damier).
            """
        raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

    def no_more_walls(self=None):
        """Plus de murs disponible pour le joueur.
        Raise:
        QuoridorError: Le joueur a déjà placé tous ses murs.
            """
        raise QuoridorError("Le joueur a déjà placé tous ses murs.")

    def wall_already_here(self=None):
        """Un mur est déjà présent sur cette position.
        Raise:
        QuoridorError: Un mur occupe déjà cette position.
            """
        raise QuoridorError("Un mur occupe déjà cette position.")

    def wrong_type_move(self=None):
        """Type de coup donné invalide.
        Raise:
        QuoridorError: Le type de coup est invalide.
            """
        raise QuoridorError("Le type de coup est invalide.")

    def incorrect_wall_orientation(self=None):
        """La position est invalide pour cette orientation.
        Raise:
        QuoridorError: La position est invalide pour cette orientation.
            """
        raise QuoridorError("La position est invalide pour cette orientation.")

    def end_of_the_game(self=None):
        """La partie est déjà terminée.
        Raise:
        QuoridorError: La position est invalide pour cette orientation.
            """
        raise QuoridorError("La partie est déjà terminée.")
