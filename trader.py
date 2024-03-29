"""
Projet démineur
Auteurs :   Mathis Bulka
            Samuel Cornier
            Léo Simon
            Sacha Trouvé

    Module trader: gestion du marchand
"""

import pygame

COIN =      -2
MAGNIFIER = -3
SHIELD =    -5
UPGRADER =  -6
RIFLE =     -10

class Trader:
    """
    The Trader class represents the in-game trader that the player can visit to purchase items.

    Attributes:
        game (Game): a reference to the main game instance
        trader_image (pygame.Surface): the image of the trader
        sign_hovered_image (pygame.Surface): the image of the trader sign when hovered
        sign_rect (pygame.Rect): the rectangle of the trader sign
        magnifier_image (pygame.Surface): the image of the magnifier item
        magnifier_rect (pygame.Rect): the rectangle of the magnifier item
        shield_image (pygame.Surface): the image of the shield item
        shield_rect (pygame.Rect): the rectangle of the shield item
        upgrader_image (pygame.Surface): the image of the upgrader item
        upgrader_rect (pygame.Rect): the rectangle of the upgrader item
    """
    def __init__(self, game):
        self.game = game
        self.trader_image = pygame.image.load(f"sprites/trader.png").convert_alpha()
        self.trader_image = pygame.transform.scale(self.trader_image, (self.game.screen_width - self.game.gui_width, self.game.screen_height))

        self.sign_hovered_image = pygame.image.load(f"sprites/sign_hovered.png").convert_alpha()
        self.sign_hovered_image = pygame.transform.scale(self.sign_hovered_image, (self.trader_image.get_width() * 22/100,
                                                                                   self.trader_image.get_height() * 20/100))

        self.sign_rect = self.sign_hovered_image.get_rect()
        self.sign_rect.x = self.game.screen_width - self.game.gui_width - self.trader_image.get_width() * 26.5/100
        self.sign_rect.y = self.game.screen_height - self.trader_image.get_height() * (102*100 / 360)/100

        self.trader_rect = pygame.Rect(0, 0, self.trader_image.get_width() * (91*100 / 600) / 100, self.trader_image.get_height() * (145*100 / 360) / 100)

        size = self.game.screen_width * 7.5 / 100
        y = self.game.screen_height / 2 + self.game.screen_height * 13 / 100

        self.magnifier_image = self.game.items[MAGNIFIER].image.copy()
        self.magnifier_image = pygame.transform.scale(self.magnifier_image, (size, size))
        self.magnifier_rect = self.magnifier_image.get_rect()
        self.magnifier_rect.x = ((self.game.screen_width - self.game.gui_width)/2 - self.game.screen_width * (1 + 14) / 100) - (self.magnifier_image.get_width() / 2)
        self.magnifier_rect.y = y

        self.shield_image = self.game.items[SHIELD].image.copy()
        self.shield_image = pygame.transform.scale(self.shield_image, (size, size))
        self.shield_rect = self.shield_image.get_rect()
        self.shield_rect.x = ((self.game.screen_width - self.game.gui_width)/2 - self.game.screen_width * 2.6 / 100) - (self.shield_image.get_width() / 2)
        self.shield_rect.y = y

        self.upgrader_image = self.game.items[UPGRADER].image.copy()
        self.upgrader_image = pygame.transform.scale(self.upgrader_image, (size, size))
        self.upgrader_image = pygame.transform.flip(self.upgrader_image, True, False)
        self.upgrader_rect = self.upgrader_image.get_rect()
        self.upgrader_rect.x = ((self.game.screen_width - self.game.gui_width)/2 - self.game.screen_width * (4 - 14) / 100) - (self.upgrader_image.get_width() / 2)
        self.upgrader_rect.y = y

    def display(self):
        """
        Draws the trader and his items on the screen.
        """
        item_y = self.game.screen_height - self.trader_image.get_height()
        self.game.screen.blit(self.trader_image, (0, 0))
        self.game.screen.blit(self.magnifier_image, (self.magnifier_rect.x, self.magnifier_rect.y))
        self.game.screen.blit(self.shield_image, (self.shield_rect.x, self.shield_rect.y))
        self.game.screen.blit(self.upgrader_image, (self.upgrader_rect.x, self.upgrader_rect.y))

    def sign_hovered(self):
        """
        Returns True if the trader sign is hovered, False otherwise.
        """
        if self.sign_rect.collidepoint(pygame.mouse.get_pos()):
            self.game.screen.blit(self.sign_hovered_image, (self.sign_rect.x, self.sign_rect.y))
            return True

        return False

    def handling_events(self):
        """
        Handles events related to the trader and his items.
        """
        if self.sign_hovered():
            self.game.is_trading = False
            self.game.run()

        elif self.magnifier_rect.collidepoint(pygame.mouse.get_pos()):# and self.game.items[COIN].amount >= 0:
            self.game.items[COIN].amount -= 10
            self.game.items[MAGNIFIER].picked()
            # self.game.item_collected.play()

        elif self.shield_rect.collidepoint(pygame.mouse.get_pos()):# and self.game.items[COIN].amount >= 0:
            self.game.items[COIN].amount -= 10
            self.game.items[SHIELD].picked()
            # self.game.item_collected.play()

        elif self.upgrader_rect.collidepoint(pygame.mouse.get_pos()):# and self.game.items[COIN].amount >= 0:
            self.game.items[COIN].amount -= 10
            self.game.items[UPGRADER].picked()
            # self.game.item_collected.play()

        elif self.trader_rect.collidepoint(pygame.mouse.get_pos()) and self.game.player.active_equipped == RIFLE:
            self.game.is_trader_dead = True