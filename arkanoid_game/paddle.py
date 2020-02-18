import pygame


class Paddle:

    def __init__(self):
        self.paddle_x = 280
        self.paddle_y = 790
        self.paddle_width = 60
        self.paddle_height = 10
        self.paddle_speed = 10
        self.collor = (255, 255, 255)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle_x = self.paddle_x - self.paddle_speed
        elif keys[pygame.K_RIGHT]:
            self.paddle_x = self.paddle_x + self.paddle_speed

    def check_screen_borders(self, screen_width):
        if self.paddle_x < 0:
            self.paddle_x = 0
        if self.paddle_x + self.paddle_width > screen_width:
            self.paddle_x = screen_width - self.paddle_width
