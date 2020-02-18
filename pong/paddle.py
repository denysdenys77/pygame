import pygame


class Paddle:

    def __init__(self):
        self.x = 585
        self.y = 285
        self.width = 15
        self.height = 30
        self.speed = 10
        self.color = (255, 255, 255)

    def set_on_screen(self, screen):
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        return self.y - self.speed

    def move_down(self):
        return self.y + self.speed