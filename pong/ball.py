import pygame


class Ball:

    def __init__(self):
        self.color = (255, 255, 255)
        self.x = 200
        self.y = 300
        self.radius = 10
        self.speed = 5

    def set_on_screen(self, screen):
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move_up_and_left(self):
        return self.x - self.speed, self.y - self.speed

    def move_down_and_right(self):
        return self.x + self.speed, self.y + self.speed

    def move_up_and_right(self):
        return self.x + self.speed, self.y - self.speed

    def move_down_and_left(self):
        return self.x - self.speed, self.y + self.speed
