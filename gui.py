"""
Projet démineur
Auteurs :   Mathis Bulka
            Samuel Cornier
            Léo Simon
            Sacha Trouvé

    Module gui: gestion de l'affichage du plateau de jeu
"""

import pygame

class Gui:
    """
    The Gui class is responsible for managing the display of the game GUI,
    including the game menu, inventory, and HUD elements.

    Parameters:
    game (Game): The Game instance that this GUI is associated with.
    gui_width (int): The width of the GUI in pixels.

    Attributes:
    game (Game): The Game instance that this GUI is associated with.
    color (tuple): The color of the GUI background.
    gui_width (int): The width of the GUI in pixels.
    offset_y (int): The vertical offset of the GUI.
    """

    def __init__(self, game, gui_width):
        self.game = game
        self.color = (135, 135, 135)
        self.gui_width = gui_width + 5
        self.offset_y = self.game.screen_height * 1/100

    def display(self):
        """
        Draw the GUI on the screen.
        """
        pygame.draw.rect(self.game.screen, self.color,
             pygame.Rect(self.game.screen_width - self.gui_width,
                         0,
                         self.gui_width, self.game.screen_height))
