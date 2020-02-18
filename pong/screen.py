import pygame


class Screen:

    def __init__(self, width=600, height=400):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))

    # def open(self):
    #     return pygame.display.set_mode((self.width, self.height))

    def fill_screen(self):
        return self.window.fill((0, 0, 0))

    def update(self):
        return pygame.display.update()
