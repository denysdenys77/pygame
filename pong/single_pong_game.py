import pygame
import random
from paddle import Paddle
from ball import Ball


class SingleGame:

    @staticmethod
    def run(paddle, ball):

        # выбор изначального направления
        ball_direction = random.choice(['move_up_and_left', 'move_down_and_right',
                                        'move_up_and_right', 'move_down_and_left'])

        pygame.init()
        screen = pygame.display.set_mode((600, 400))

        while True:

            

            # выход из игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # управление ракеткой
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                paddle.move_up()
            elif keys[pygame.K_DOWN]:
                paddle.move_down()

            # движение мяча и переопределение направления
            if ball_direction is 'move_up_and_left':
                ball.move_up_and_left()
                ball_direction = 'move_up_and_left'
            elif ball_direction is 'move_down_and_right':
                ball.move_down_and_right()
                ball_direction = 'move_down_and_right'
            elif ball_direction is 'move_up_and_right':
                ball.move_up_and_right()
                ball_direction = 'move_up_and_right'
            elif ball_direction is 'move_down_and_left':
                ball.move_down_and_left()
                ball_direction = 'move_down_and_left'

            # изменение траектории при столкновении со стеной
            if ball.x <= 0 and ball_direction is 'move_down_and_right':
                ball_direction = 'move_down_and_left'
            elif ball.x <= 0 and ball_direction is 'move_up_and_right':
                ball_direction = 'move_up_and_left'

            elif ball.y <= 0 and ball_direction is 'move_up_and_right':
                ball_direction = 'move_down_and_right'
            elif ball.y <= 0 and ball_direction is 'move_up_and_left':
                ball_direction = 'move_down_and_left'

            elif ball.y >= 225 and ball_direction is 'move_down_and_right':
                ball_direction = 'move_up_and_right'
            elif ball.y >= 225 and ball_direction is 'move_down_and_left':
                ball_direction = 'move_up_and_left'

            # изменение траектории при столкновении с ракеткой
            if ball.x + (ball.radius * 2) >= paddle.x and ball.y in range(paddle.y, paddle.y + paddle.height) and \
                    ball_direction is 'move_up_and_right':
                ball_direction = 'move_up_and_left'
            elif ball.x + (ball.radius * 2) >= paddle.x and ball.y in range(paddle.y, paddle.y + paddle.height) and \
                    ball_direction is 'move_down_and_right':
                ball_direction = 'move_down_and_left'

            screen.fill((0, 0, 0))
            paddle.set_on_screen(screen)
            ball.set_on_screen(screen)
            pygame.display.update()







