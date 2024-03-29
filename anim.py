"""
Projet démineur
Auteurs :   Mathis Bulka
            Samuel Cornier
            Léo Simon
            Sacha Trouvé

    Module anim: gestion des animations du jeu
"""

import pygame

class Spritesheet:
    """
    A class to handle animations thanks to Spritesheet.

    Parameters:
        filename (str): The path to the Spritesheet image file.
        sprite_sheet_width (int): The width of each sprite in the Spritesheet.
        sprite_sheet_height (int): The height of each sprite in the Spritesheet.

    Attributes:
        file (pygame.Surface): The loaded Spritesheet image.
        sprite_sheet_width (int): The width of each sprite in the Spritesheet.
        sprite_sheet_height (int): The height of each sprite in the Spritesheet.
        animation (list): A list of all the frames of the animation.
    """

    def __init__(self, filename: str, sprite_number_x: int, sprite_number_y: int, scale: tuple[int, int], fps: int):
        self.filename = filename
        self.file = pygame.image.load(filename).convert_alpha()
        self.sprite_number_x = sprite_number_x
        self.sprite_number_y = sprite_number_y
        self.sprite_dimensions = (self.file.get_width() // self.sprite_number_x, self.file.get_height() // self.sprite_number_y)
        self.line = 0
        self.sprite_index = 0
        self.scale = scale
        self.image = self.file.subsurface(0, 0, self.sprite_dimensions[0], self.sprite_dimensions[1])
        self.image = pygame.transform.scale(self.image, self.scale)
        self.delay = 1000 / fps
        self.time = 0
        self.lock_anim = False

    def make_anim(self, line: int, start_frame: int, end_frame: int, fps: int = None, loop: list[bool, int] = [True, 0]):
        """
        Create an animation from a specific line of the Spritesheet.

        Args:
            line (int): The line number of the Spritesheet to use for the animation.
            number_frames (int): The number of frames in the animation.
            fps (int): The frames per second of the animation.

        Returns:
            list: A list of all the frames of the animation.
        """
        if fps != None:
            self.delay = 1000 / fps

        if line != self.line:
            self.sprite_index = start_frame
            self.line = line

        end_frame += 1
        current_time = pygame.time.get_ticks()

        if current_time - self.time > self.delay:
            self.time = current_time

            width = self.sprite_dimensions[0]
            height = self.sprite_dimensions[1]
            x = (self.sprite_index % end_frame + start_frame) * width
            y = line * height
            self.image = self.file.subsurface(x, y, width, height)
            self.image = pygame.transform.scale(self.image, self.scale)

            if not self.lock_anim:
                if (not loop[0]) and self.sprite_index >= end_frame - loop[1]:
                    self.lock_anim = True
                    self.sprite_index = end_frame - loop[1]

                else:
                    self.sprite_index += 1

        return self.image

    def get(self):
        """
        Draw an animation frame on the screen.

        Args:
            None

        Returns:
            None
        """
        return self.image