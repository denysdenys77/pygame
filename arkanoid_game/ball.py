import random


class Ball:

    def __init__(self):
        self.ball_x = 200
        self.ball_y = 300
        self.ball_radius = 5
        self.ball_speed = 5
        self.color = (255, 255, 255)
        self.ball_direction = random.choice(['move_up_and_left', 'move_down_and_right',
                                             'move_up_and_right', 'move_down_and_left'])

    def move(self):
        if self.ball_direction is 'move_up_and_left':
            self.ball_x = self.ball_x - self.ball_speed
            self.ball_y = self.ball_y - self.ball_speed
        elif self.ball_direction is 'move_down_and_right':
            self.ball_x = self.ball_x + self.ball_speed
            self.ball_y = self.ball_y + self.ball_speed
        elif self.ball_direction is 'move_up_and_right':
            self.ball_x = self.ball_x + self.ball_speed
            self.ball_y = self.ball_y - self.ball_speed
        elif self.ball_direction is 'move_down_and_left':
            self.ball_x = self.ball_x - self.ball_speed
            self.ball_y = self.ball_y + self.ball_speed

    def check_screen_borders(self, screen_width):
        if self.ball_x - self.ball_radius <= 0 and self.ball_direction is 'move_up_and_left':
            self.ball_direction = 'move_up_and_right'
        elif self.ball_x - self.ball_radius <= 0 and self.ball_direction is 'move_down_and_left':
            self.ball_direction = 'move_down_and_right'
        elif self.ball_y - self.ball_radius <= 0 and self.ball_direction is 'move_up_and_right':
            self.ball_direction = 'move_down_and_right'
        elif self.ball_y - self.ball_radius <= 0 and self.ball_direction is 'move_up_and_left':
            self.ball_direction = 'move_down_and_left'
        elif self.ball_x + self.ball_radius >= screen_width and self.ball_direction is 'move_down_and_right':
            self.ball_direction = 'move_down_and_left'
        elif self.ball_x + self.ball_radius >= screen_width and self.ball_direction is 'move_up_and_right':
            self.ball_direction = 'move_up_and_left'

    def check_paddle_hit(self, paddle):
        if self.ball_y + self.ball_radius == paddle.paddle_y and self.ball_x in range(paddle.paddle_x, paddle.paddle_x + paddle.paddle_width) and \
                self.ball_direction is 'move_down_and_right':
            self.ball_direction = 'move_up_and_right'
        elif self.ball_y + self.ball_radius == paddle.paddle_y and self.ball_x in range(paddle.paddle_x, paddle.paddle_x + paddle.paddle_width) and \
                self.ball_direction is 'move_down_and_left':
            self.ball_direction = 'move_up_and_left'
