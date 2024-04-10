import pygame

class Speech_bubble:
    """
    Manages the creation and display of text bubbles.
    """
    def __init__(self, game, speech: str):
        """
        Initialize the object.
        """
        self.game = game
        self.bubble_image = pygame.image.load("sprites/bubble.png").convert_alpha()
        self.spike_image = pygame.image.load("sprites/spike.png").convert_alpha()
        self.change_speech(speech)
        self.initial_time = pygame.time.get_ticks()

    def display(self):
        """
        Display the bubble with the text inside.
        """
        if self.initial_time + len(self.speech_list) * self.delay >= pygame.time.get_ticks():
            if self.game.is_trading:
                bubble_position = (self.game.screen_width * 42/100 - self.bubble_image.get_width(),
                                   self.game.screen_height * 38/100 - self.bubble_image.get_height())
                spike_position = (self.game.screen_width * 42/100 - self.spike_image.get_width(),
                                  self.game.screen_height * 38/100)
                self.game.screen.blit(self.bubble_image, bubble_position)
                self.game.screen.blit(self.spike_image, spike_position)

                for speech_index in range(len(self.speech_list)):
                    text_image = self.font.render(self.speech_list[speech_index], True, (0, 0, 0))
                    text_position = (self.game.screen_width * 42/100 - self.bubble_image.get_width() * 95/100,
                                     self.game.screen_height * 38/100 - self.bubble_image.get_height() + speech_index * text_image.get_height() + self.bubble_image.get_height() * 5/100)
                    self.game.screen.blit(text_image, text_position)

            else:
                bubble_position = (self.game.player.x - self.bubble_image.get_width() * 90/100,
                                   self.game.player.y - self.bubble_image.get_height() + self.game.gui_width * 1 / 2)
                spike_position = (self.game.player.x + self.bubble_image.get_width() * 10/100 - self.spike_image.get_width(),
                                  self.game.player.y + self.game.gui_width * 1 / 2)
                self.game.screen.blit(self.bubble_image, bubble_position)
                self.game.screen.blit(self.spike_image, spike_position)

                for speech_index in range(len(self.speech_list)):
                    text_image = self.font.render(self.speech_list[speech_index], True, (0, 0, 0))
                    text_position = (self.game.player.x - self.bubble_image.get_width() * 90/100 + self.bubble_image.get_width() * 5/100,
                                     self.game.player.y - self.bubble_image.get_height() + self.game.gui_width * 1 / 2 + speech_index * text_image.get_height() + self.bubble_image.get_height() * 5/100)
                    self.game.screen.blit(text_image, text_position)

    def change_speech(self, speech):
        self.speech = speech
        self.initial_time = pygame.time.get_ticks()

        length = 0
        self.delay = 0
        self.speech_list = []
        new_speech = ""
        splitted_speech = self.speech.split()
        is_speech_short = False

        if len(splitted_speech) < 20:
            new_speech = self.speech
            self.speech_list.append(new_speech)
            is_speech_short = True

        else:
            for word in range(len(splitted_speech)):
                length += len(splitted_speech[word])

                if length <= 20:
                    new_speech += splitted_speech[word] + " "
                    if len(splitted_speech) - word <= 1:
                        self.speech_list.append(new_speech)

                else:
                    new_speech += splitted_speech[word]
                    self.speech_list.append(new_speech)
                    length = 0
                    new_speech = ""

        index = -1
        maxi = len(self.speech_list[index])
        longer_element = self.speech_list[index]

        for i in range(len(self.speech_list)):
            index += 1
            if len(self.speech_list[i]) >= maxi:
                maxi = len(self.speech_list[index])
                longer_element = self.speech_list[index]

        self.font_size = round(self.game.square_size * 30/100)
        self.font = pygame.font.SysFont("Arial", self.font_size)
        text_image = self.font.render(longer_element, True, (0, 0, 0))
        width = text_image.get_width() * 1.2
        height = text_image.get_height() * 1.1 * len(self.speech_list)
        self.bubble_image = pygame.transform.smoothscale(self.bubble_image, (width, height))

        if is_speech_short:
            self.delay = 5000
        else:
            self.delay = 1600
